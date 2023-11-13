# -*- coding:utf-8 -*-
# Author: ranpeng
# Date: 2023/11/9


import numpy as np
import pandas as pd

from functools import cached_property, lru_cache
from tqdm import tqdm
from operator import itemgetter

def LAST_VALID(mat: np.ndarray) -> (np.ndarray, np.ndarray):
    ''' each column 最后一个非nan的位置和值,  如果没有就返回最后一排的值'''
    is_valid = ~np.isnan(mat)
    idxpos = mat.shape[0] - 1 - is_valid[::-1].argmax(0)
    values = mat[idxpos, range(mat.shape[1])]
    return idxpos, values

class CiticsInd:
    '''中信行业特征生成'''

    def __init__(self, ctx):
        self.ctx = ctx
        self.df = ctx.ds('ashareindustriesclasscitics').get_df(index=False)
        self.indcode_df = ctx.ds('ashareindustriescode').get_df(index=False)
        self.df.rename(columns={'entry_dt': 'indate', 'remove_dt': 'outdate'}, inplace=True)
        self.df['lev1'] = self.df['citics_ind_code'].str[:4]
        self.df['lev2'] = self.df['citics_ind_code'].str[:6]
        self.df['lev3'] = self.df['citics_ind_code'].str[:8]

    def get_ndns(self, levelnum=1):
        '''中信一级分类'''
        ndns_df = self.ctx.get_ind(self.df, on=f'lev{levelnum}')
        return ndns_df

    def lev_map(self, level=1):
        lev1_codes = np.unique(self.df[f'lev{level}'])
        result = []
        for i, code in enumerate(lev1_codes):
            cond1 = self.indcode_df['levelnum'] == level + 1
            cond2 = self.indcode_df['industriescode'].str.startswith(code)
            ind_name = self.indcode_df[cond1 & cond2]['industriesname'].values[0]
            result.append((code, i, ind_name))
        return result


class FdmLib:
    '''处理基本面相关数据, 只处理0331,0630,0930,1231
    408001000, 408005000代表大的修改
    '''

    def __init__(self, ctx):
        self.ctx = ctx
        self._income_dset = ctx.ds('ashareincome')
        self._cashflow_dset = ctx.ds('asharecashflow')
        self._balance_dset = ctx.ds('asharebalancesheet')
        self._notice_dset = ctx.ds('ashareprofitnotice')
        self._express_dset = ctx.ds('ashareprofitexpress')
        self.primary_keys = self._income_dset.primary_keys()
        self.feature_info = self._get_feature_info()

        self.features = {}
        self.nqns_df = None  # 用于检查nqns_compute后最后一个nqns_mat结果

    def _get_feature_info(self):
        '''获取feature的描述信息'''
        column_des = []
        column_des += [(k, 'income', v) for k, v in self._income_dset.column_des(index=False).items()]
        column_des += [(k, 'cashflow', v) for k, v in self._cashflow_dset.column_des(index=False).items()]
        column_des += [(k, 'balance', v) for k, v in self._balance_dset.column_des(index=False).items()]
        return pd.DataFrame(column_des, columns=['feature', 'dset', 'des'])

    def concat(self, *args):
        '''把多特征merge在一起, 去重,有先保留前面的特征'''
        df = pd.concat(args)
        df.drop_duplicates(keep='first', inplace=True)
        df.sort_index(inplace=True)
        return df

    @cached_property
    def income_df(self):
        df = self.process_fdm(self._income_dset.get_df())
        return df

    @cached_property
    def cashflow_df(self):
        df = self.process_fdm(self._cashflow_dset.get_df())
        return df

    @cached_property
    def balance_df(self):
        df = self.process_fdm(self._balance_dset.get_df())
        return df

    @cached_property
    def notice_df(self):
        df = self.process_fdm(self._notice_dset.get_df())
        return df

    @cached_property
    def express_df(self):
        df = self.process_fdm(self._express_dset.get_df())
        return df

    def process_fdm(self, df):
        '''预先处理三大表的基础数据'''
        if 'statement_type' in df.columns:
            df = df[df.statement_type.isin([408001000, 408005000])]
        df = df[df.index.get_level_values('stockcode').isin(self.ctx.instruments)]
        ann_dt = df.index.get_level_values('ann_dt')
        report_period = df.index.get_level_values('report_period')
        # 部分并购事件导致公布的 report period不一定是季度末
        df = df[
            (ann_dt >= self.ctx.start_dt) & (ann_dt <= self.ctx.end_dt) & (report_period.isin(self.ctx.report_periods))]
        return df

    def nqns_compute(self, expression, *args, ffill=True, ndns=False, **kwargs):
        '''滚动ann_dt, apply func on nqns_mat
        expression: 输入是nqns, 输出为ns
        args: 需要参与计算的特征名
        return: 返回nsnanq抽
        '''
        for i in kwargs:
            exec(f"{i}=kwargs[i]")  # 注册变量
        fdmds_d = dict([(k, FdmDs(v, self.ctx)) for k, v in self.features.items() if k in args])  # 表达式必需的变量
        nqns_mats = dict([(k, self.ctx.nqns_mat.copy()) for k, v in self.features.items() if k in args])
        nan_mask = np.full((self.ctx.nq, self.ctx.ns), 1.0)
        for k in args:
            expression = expression.replace(k, f"nqns_mats['{k}']")
        ctx = self.ctx  # 有用，别删
        nans_df = {}
        for dt in tqdm(self.ctx.ann_dts):
            compute = False
            for name, fdmds in fdmds_d.items():
                if fdmds.is_avaiable(dt):
                    fdmds.set_nqns(dt, nqns_mats[name])
                    compute = True
            if compute:
                a = [v.last_q for k, v in fdmds_d.items()]
                b = np.vstack(a)
                last_q = np.min(b, axis=0)
            else:
                continue
            nqns_result = eval(expression)
            # filter nan
            for j, v in enumerate(last_q):
                nqns_result[v + 1:, j] = np.nan
            _, ns_result = LAST_VALID(nqns_result)
            nans_df[dt] = ns_result
        result = pd.DataFrame(nans_df, index=ctx.instruments).T
        # v1.4 新增
        self.nqns_df = pd.DataFrame(nqns_result, index=ctx.report_periods, columns=ctx.instruments)  # 用于检查
        if ffill:
            result = result.reindex(index=ctx.ann_dts).ffill()
        if ndns:
            result = ctx.nans2ndns(result)
        return result

    # v1.7 wp
    def nsnanq_exp(self, expression, **kwargs):
        '''滚动ann_dt, apply func on nqns_mat
        kwargs：里面可以是函数， 可以是特征
        expression: 输入是nansnq_ds, 输出也是输入是nansnq_ds
        args: 需要参与计算的特征序列需要
        '''
        fdmds_d = {}
        nqns_mats = {}
        for k in kwargs:
            v = kwargs[k]
            # 注册函数
            if callable(v):
                exec(f"{k}=v")
            # 注册变量
            else:
                fdmds_d[k] = FdmDs(v, self.ctx)
                nqns_mats[k] = self.ctx.nqns_mat.copy()
                new_expression = expression.replace(k, f"nqns_mats['{k}']")
        ctx = self.ctx  # 有用，别删
        df_list = []
        for dt in tqdm(ctx.ann_dts):
            compute = False
            for name, fdmds in fdmds_d.items():
                if fdmds.is_avaiable(dt):
                    fdmds.set_nqns(dt, nqns_mats[name])
                    compute = True
            if not compute:
                """没有新的事件"""
                continue
            nqns_result = eval(new_expression)
            row_i, ns_result = LAST_VALID(nqns_result)
            rps = ctx.report_periods[row_i]
            valid_mask = ~np.isnan(ns_result)
            sub_df = pd.DataFrame({'report_period': rps[valid_mask], 'ann_dt': dt, expression: ns_result[valid_mask],
                                   'stockcode': ctx.instruments[valid_mask]})
            df_list.append(sub_df)
        df = pd.concat(df_list).set_index(ctx.nansnq_pkeys).sort_index()
        ds = df[expression]
        return ds

    # v1.4 author wp: 增加name和检查valid_data功能
    def add_feature(self, ds, name):
        '''添加基本面特征'''
        ds.name = name
        ds = ds.dropna()
        self.features[name] = ds

    def clear_features(self):
        self.features = {}


class FdmDs:
    '''单nansnq特征处理'''

    def __init__(self, ds, ctx):
        self.ctx = ctx
        self.name = ds.name
        self.ds = ds.dropna()
        self.v = self.ds.values
        self.na_loc, self.nq_loc, self.ns_loc = self.get_loc()
        self.ann_dts = self.ds.index.get_level_values('ann_dt')
        self.unique_anndt = np.unique(self.ann_dts)

        self.last_q = np.full(ctx.ns, -1)  # nqns中每列最后一个available值的位置
        self.nqns_funcs = []

    def get_loc(self):
        '''获取nqns mat上的位置信息'''
        idx = self.ds.index
        nq_locs = idx.get_level_values('report_period').map(self.ctx.nq_dict)
        ns_locs = idx.get_level_values('stockcode').map(self.ctx.ns_dict)
        na_locs = idx.get_level_values('ann_dt').map(self.ctx.na_dict)
        return na_locs.astype(int), nq_locs.astype(int), ns_locs.astype(int)

    # @timer
    def is_avaiable(self, dt):
        '''在dt这天是否有数据'''
        return dt in self.unique_anndt

    # @timer
    def set_nqns(self, dt, nqns_mat):
        '''更新nqns_mat数据， 并更新最后位置, 注意可能会更新之前的数据'''
        mask = self.ann_dts == dt

        v = self.v[mask]
        nq_loc = self.nq_loc[mask]
        ns_loc = self.ns_loc[mask]

        # 更新值
        nqns_mat[nq_loc, ns_loc] = v

        # 更新最后一个nq的位置
        for i in range(len(nq_loc)):
            q_loc = nq_loc[i]
            s_loc = ns_loc[i]
            if q_loc > self.last_q[s_loc]:
                self.last_q[s_loc] = q_loc

    def to_df(self, nqns_mat):
        return pd.DataFrame(nqns_mat, index=self.ctx.report_periods, columns=self.ctx.instruments)

    def register(self, funcs):
        '''注册要使用的nqns函数'''
        pass

    def compute(self):
        '''触发计算，返回nans_df'''
        nans_df = 1
        return nans_df


class DivLib:
    '''分红相关数据处理'''

    def __init__(self, ctx):
        print('initalizing DivLib')
        self.ctx = ctx
        self.cols = ['div_progress', 'cash_div_pretax', 'div_object', 'div_baseshare', 'report_period']
        self.divd_df = self.ctx.asharedividend[self.cols].reset_index().set_index(
            ['stockcode', 'ann_dt', 'report_period'])
        self.divd_df = self.preprocess(self.divd_df)  # index is duplicated, 由于分红对象不同

        self.stockcode_idx = self.divd_df.index.get_level_values('stockcode')
        self.ann_dt_idx = self.divd_df.index.get_level_values('ann_dt')
        self.report_period_idx = self.divd_df.index.get_level_values('report_period')
        self.report_year_idx = (self.report_period_idx / 10000).astype(int)

        self.stockcodes = self.stockcode_idx.unique()
        self.ann_dts = self.ann_dt_idx.unique()
        self.report_periods = self.report_period_idx.unique()
        self.report_years = self.report_year_idx.unique()
        print('DivLib ready!!')

    def year_end_idx(self, mmdd):
        '''生成每年年底的确认事件'''
        mat_df = pd.DataFrame(0.0, index=self.stockcodes, columns=(self.report_years * 10000) + mmdd)
        df = mat_df.unstack(level=1).to_frame()
        df['ann_dt'] = df.index.get_level_values('report_period') + 10000
        idx = df.reset_index().set_index(['stockcode', 'ann_dt', 'report_period']).index
        return idx

    def preprocess(self, divd_df):
        '''预处理基础数据'''
        divd_df = divd_df[(divd_df['div_progress'] == '3') & (divd_df['cash_div_pretax'] > 0)]
        divd_df['divd'] = (divd_df['cash_div_pretax'] * divd_df['div_baseshare']).values
        return divd_df

    def divd_w_agg(self):
        '''聚合divd'''
        index_names = self.divd_df.index.names
        divd_df = self.divd_df.groupby(self.divd_df.index).agg({
            'divd': sum})
        divd_df.index = pd.MultiIndex.from_tuples(divd_df.index, names=index_names)
        return divd_df

    @lru_cache
    def lyr_divd(self):
        '''静态分红(去年全年税前分红): 每年分红确定的时间为ann_dt|已经比对wind F9'''
        divd_df = self.divd_w_agg()
        # 剔除duplicate index
        # 加入年底确认事件
        new_ds = pd.Series(0.0, index=self.year_end_idx(1231))
        merged_divd_ds = pd.concat([divd_df['divd'], new_ds]).sort_index()

        nsnq_idx = merged_divd_ds.index.droplevel('ann_dt')
        merged_report_years_idx = (merged_divd_ds.index.get_level_values('report_period') / 10000).astype(int)
        merged_stockcode_idx = merged_divd_ds.index.get_level_values('stockcode')
        cum_divd_ds = merged_divd_ds.groupby(by=[merged_stockcode_idx, merged_report_years_idx]).transform(np.nancumsum)
        cum_divd_ds = cum_divd_ds[~nsnq_idx.duplicated(keep='first')]
        # cum_divd_ds[cum_divd_ds.index.get_level_values('stockcode') == '000001.SZ']
        year_end = cum_divd_ds.index.get_level_values('report_period').astype(str).str[4:] == '1231'
        df = cum_divd_ds[year_end]
        return self.ctx.valid_data(df)

    def divd_ratio(self):
        '''静态分红/年底总市值'''
        df = self.lyr_divd().to_frame(name='static_divd')
        tot_mv = self.ctx.dev_nans_stkbase['nans_totmv']
        df['tot_mv'] = tot_mv[df.index.droplevel('ann_dt')].values
        df['static_divd_ratio'] = df['static_divd'] / df['tot_mv']
        return df['static_divd_ratio']

    def div_payout(self):
        '''股息支付率: 年度分红/年报归母净利润'''
        # 在外部结合FdmLib使用
        return


class ConforeStk:
    '''朝阳永续：一致预期数据 con_forecast_stk
    rpt_forecast_stk：最原始的数据,基于每个分析师报告
    con_forecast_stk: con代表一致预期（分析师结果加权）
        con_year: 基准和预测年
        [con_or_type, con_np_type, con_eps_type]：0：真实财报(26%)  1:90天内有5家以上有数据(17%)
            2:120天内手工估算(29%);3:沿用历史数据(19%);4：数据模拟 : 0,1,2以外不建议使用
            注意：！！2021年5月1日期， 3,4 类型交换顺序！！！
        [con_or_hisdate，con_np_hisdate，con_eps_hisdate]: 当上面type==3的时候才用
        各种类型控制的特征：
            con_or_type： con_or，con_or_yoy
            con_np_type： con_np，con_na, con_roe,con_np_yoy,con_npcgrate_2y,con_npgrate_1w,
                          con_npgrate_1w,con_npgrate_4w,con_npgrate_13w,con_npgrate_26w,con_npgrate_52w
            con_eps_type： con_eps，con_pe, con_peg
            con_np_type & con_eps_type: con_ps, con_pb
    con_forecast_roll_stk:
        基于con_forecast_stk的进一步加工，roll代表滚动前看一年（doc文档描述有误）
        时间加权： m/365
    con_date：和trade_dt结构一致
    一致预期股息率： wind有，朝阳永续只有基础数据
    关于5月1日换基准年：每日就给4个con_year， 如果年报出来，就删除最后一个！！
    '''

    def __init__(self, ctx):
        print('init ConforeStk...')
        self.ctx = ctx
        self.p_keys = ['stockcode', 'ann_dt']
        self.feature_map = {
            'or': ['con_or', 'con_or_yoy'],
            'np': ['con_np', 'con_na', 'con_roe', 'con_np_yoy', 'con_npcgrate_2y', 'con_npgrate_1w',
                   'con_npgrate_1w', 'con_npgrate_4w', 'con_npgrate_13w', 'con_npgrate_26w', 'con_npgrate_52w'],
            'eps': ['con_eps', 'con_pe', 'con_peg'],
            'np_eps': ['con_ps', 'con_pb'],
        }
        self.feature_info = self.get_feature_info()
        self.con_types = [0, 1, 2]  # 需要保留的数据类型
        self.df, self.nd_loc, self.ns_loc, self.ny_loc = self.preprocess()  # 需要20G内存
        self.ndns_bench_locs = self.get_ndns_bench_locs()  # 基准年都是一样的
        print('init ConforeStk... ready!!')

    def preprocess(self):
        '''con_forecast_stk dataframe'''
        filters = itemgetter(0, 1, 4)(self.ctx.parquet_filters)
        df = self.ctx.con_forecast_stk.get_df(filters=filters)
        df['n_year'] = 1
        df['n_year'] = df['n_year'].groupby(level=[0, 1]).cumsum() - 1  # 太慢了
        nd_loc = df.index.get_level_values('trade_dt').map(self.ctx.nd_dict).values
        ns_loc = df.index.get_level_values('stockcode').map(self.ctx.ns_dict).values
        ny_loc = df['n_year'].values
        return df, nd_loc, ns_loc, ny_loc

    def get_ndns_bench_locs(self):
        '''获取基准年的位置'''
        self.nan_univ = np.clip(self.ndnsny_nptype.sum(axis=-1), 1, 1)
        self.year1_loc = (self.ndnsny_nptype != 0).argmax(axis=-1) * self.nan_univ  # 基准年后1年
        self.year0_loc = self.year1_loc - 1
        self.year2_loc = self.year1_loc + 1
        self.year3_loc = self.year1_loc + 2

    def d3mat(self, fill=np.nan):
        '''3d 空矩阵'''
        return np.full([self.ctx.nd, self.ctx.ns, 4], fill_value=fill)

    @cached_property
    def ndnsny_ortype(self):
        return self.to_ndnsny(self.df['con_or_type'])

    @cached_property
    def ndnsny_nptype(self):
        return self.to_ndnsny(self.df['con_np_type'])

    @cached_property
    def ndnsny_epstype(self):
        return self.to_ndnsny(self.df['con_eps_type'])

    @cached_property
    def np_df(self):
        '''con_np_type 类型为主的数据与衍生数据'''
        cols = ['con_np_type'] + self.feature_map['np']
        return self.df[cols]

    @cached_property
    def eps_df(self):
        '''con_eps_type 类型为主的数据与衍生数据'''
        cols = ['con_eps_type'] + self.feature_map['eps']
        return self.df[cols]

    @cached_property
    def or_df(self):
        '''con_or_type 类型为主的数据与衍生数据'''
        cols = ['con_or_type'] + self.feature_map['or']
        return self.df[cols]

    def get_feature(self, feature):
        '''获取单列特征'''
        df_name = self.feature_info['con_type'][feature]
        df = eval(f'self.{df_name}_df')
        return df[feature]

    def get_feature_info(self):
        '''获取所有的特征信息'''
        cols = ['con_type', 'table_name', 'description']
        result = [pd.Series(k, index=v) for k, v in self.feature_map.items()]
        result = pd.concat(result).to_frame('con_type')
        result['table_name'] = 'con_forecast_stk'
        result['description'] = result.index.map(self.ctx.con_forecast_stk.column_des())
        return result[cols]

    def get_ndnsny(self, feature):
        '''获取三维特征 ndnsny'''
        ds = self.get_feature(feature)
        return self.to_ndnsny(ds)

    def to_ndnsny(self, ds):
        '''把列数据进行三维转换ndnsny'''
        result = self.d3mat()
        result[self.nd_loc, self.ns_loc, self.ny_loc] = ds.values
        return result

    def year0(self, ds):
        '''最后基准年后1年的数据
        n : 0， 基准年， 1，预测第一年  2，预测第二年， 3，预测第三年
        '''
        ndnsny_ds = self.to_ndnsny(ds)
        self.year0_loc[self.year0_loc < 0] = np.nan
        ndnsny_ds = 1
        return ndnsny_ds

    def year1(self, ds):
        '''获取基准年后1年的数据
        n : 0， 基准年， 1，预测第一年  2，预测第二年， 3，预测第三年
        '''
        ndnsny_ds = self.to_ndnsny(ds)
        return ndnsny_ds

    def year2(self, ds):
        '''获取基准年后n年的数据
        n : 0， 基准年， 1，预测第一年  2，预测第二年， 3，预测第三年
        '''
        ndnsny_ds = self.to_ndnsny(ds)
        return ndnsny_ds

    def forward_roll(self, feature, n_year):
        '''滚动向前多少年， 时间加权
        n_year： 离当前交易日的距离
        '''
        ds = self.get_feature(feature)
        report_periods = (ds.index.get_level_values('con_year') * 10000 + 1231).astype(int)
        ctms = self.ctx.delta_dt(report_periods, ds.index.get_level_values('ann_dt'))
        return


class NpRolling:
    """numpy rolling"""

    def __init__(self, data, n):
        self.nd, self.ns = data.shape
        self.n = n

    def apply(self, func):
        """按行分别rolling"""
        for i in tqdm(range(self.nd)):
            for j in range(self.ns):
                pass

    @staticmethod
    def test_func(arr):
        """函数样例"""
        return np.nansum(arr) / np.nansum(arr)


class WindConsensus:
    """
    wind一致预期与分析师数据介绍:
        分析师基础数据
            ASHAREEARNINGEST： 个股分析盈利相关预测明细， eps， 股息率， roe， 财报相关预测的
            ASHAREIPOPRICINGFORECAST： 个股中国A股上市定价预测
            ASHARESTOCKRATING： 个股评级明细数据
        衍生一致预期数据：
            中国A股盈利预测汇总ASHARECONSENSUSDATA(对应朝阳永续ConForecast表):
                FY0：基准年， FY1：预测第一年， FY2：预测第二年
                综合值周期类型：（30/90/180/180L） 向前看的天数， L代表业绩时间事件后的预测计算而来
            中国A股一致预测个股滚动指标   ASHARECONSENSUSROLLINGDATA
                介绍：回看180天找机构最近一次预测， 对机构进行平均，每日滚动生成
                FTTM： 滚动前看12个月
                YOY: FY1相对于FY0的同比增速
                YOY2： FY2相对于FY1的同比增速
    """

    def __init__(self):
        pass


class NewSwInd:
    """新申万行业分类"""

    def __init__(self):
        pass


class InstHolding:
    """机构在股票上的持仓
    参考： wind主力持仓
    数据源：wind.
    对象包含：
        1. 国家队持仓
        2. 社保基金持仓
        3. 公募持仓
        4. 券商持仓
        5. QDII
        6. 阳光私募
        7. 北上
    特征包含：[持仓市值， 持仓变动， 持仓占流通股比例]
    """

    def __init__(self):
        pass


class ShareHolderStrut:
    """股东结构"""

    def __init__(self):
        pass


class BarraCne5:
    """barra相关的数据和函数
    回归的逻辑在《barra_risk_model_handbook》
    https://roycheng.cn/files/riskModels/barra_risk_model_handbook.pdf
    https://zhuanlan.zhihu.com/p/38280638
    参考财通证券金工：
        《“星火”多因子系列（一）：Barra 模型初探：A 股市场风格解析》
        《“星火”多因子系列（二）：Barra 模型进阶：多因子风险预测》
        《“星火”多因子系列（三）：Barra 模型深化：纯因子组合构建 》
    """

    def __init__(self, ctx, univ='univ_all'):
        self.ind = 'citics_lev1'  # 选择中信一级行业

    def pure_factor_port(self):
        """因子的投资组合对目标因子有 1 个单位的暴露，对其他因子没有暴露; 可投资性低"""
        # https://bigquant.com/wiki/doc/yinzi-moxing-MlcLesDHy5 纯因子
        # https: // zhuanlan.zhihu.com/p/96536721

        pass

    def monthly_cross_ols(self):
        '''Barra 采用期初的因子暴露取值（等价于 T - 1 期期末的因子暴露取值）和股票在 T 期内的收益率进行截面回归
        回归带截距项， 我们采用加权wls（权重为sqrt(流通市值)）进行截面回归
        '''
        pass


if __name__ == '__main__':
    pass

