from cscdata.localdata.context import CoContext
import cscdata.localdata as localdata
from functools import cached_property
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re
from utils import retry, context_data
from lib import *
from joblib import Parallel, delayed

today = int(datetime.today().strftime("%Y%m%d"))
yesterday = int((datetime.today() - timedelta(days=1)).strftime("%Y%m%d"))


class FuntContext(CoContext):
    def __init__(self, start_dt=20070101, end_dt=20231030):
        super().__init__(start_dt, end_dt)

        self.start_dt = start_dt
        self.end_dt = end_dt

        self.callib = None
        self.all_dts = None  # 1990年以来所有的日历日   # v1.4
        self.cn_tds = None  # 1990年以来过去未来全部交易日
        self.ann_dts = None  # [start_dt, end_dt]之间的所有日期日
        self.trade_dts = None  # [start_dt, end_dt]之间的所有交易日
        self.instruments = None  # [start_dt, end_dt]之间的所有上市股票

    @cached_property
    def wind_cal(self):
        return self.ds('cfuturescalendar').get_df(index=False)

    @cached_property
    def wind_des(self):
        return self.ds('cfuturesdescription').get_df(index=False)

    @cached_property
    def wind_cont_chg(self):
        return self.ds('cfuturescontprochange').get_df(index=False)

    @cached_property
    def wind_cont(self):
        return self.ds('cfuturescontpro').get_df(index=False)

    @cached_property
    def wind_eod_idx(self):
        return self.ds('cindexfutureseodprices').get_df(index=False)

    @cached_property
    def wind_eod_com(self):
        return self.ds('ccommodityfutureseodprices').get_df(index=False)

    @cached_property
    def wind_eod_bond(self):
        return self.ds('cbondfutureseodprices').get_df(index=False)

    @cached_property
    def wind_margin(self):
        return self.ds('cfuturesmarginratio').get_df(index=False)

    @cached_property
    def wind_limit(self):
        return self.ds('cfuturespricechangelimit').get_df(index=False)

    @context_data
    def get_calendars(self):
        """所有交易日"""
        df = self.wind_cal.copy()
        calendars = df.trade_dt.unique()
        calendars.sort()
        calendars = pd.DataFrame(data=calendars)
        return calendars

    def for_debug(self):
        df = 0
        return 0

    @context_data
    def get_instruments(self):
        """获取合约信息（名称+时间）"""
        df = self.wind_des.copy()
        df = df[['futcode', 'list_dt', 'delist_dt', 'contract_type']].reset_index()
        # 合约筛选
        df = select_contract(df)
        # map2symbol
        wind2symbol(df)
        # 检查合约变化
        # check_contract(df)
        contracts = df[['symbol', 'futcode', 'list_dt', 'delist_dt']]
        return contracts

    @context_data
    def get_full_index(self):
        instruments = self.get_instruments()
        instruments.rename(columns={0: 'symbol', 1: 'futcode', 2: 'start_date', 3: 'end_date'}, inplace=True)
        calendars = self.get_calendars()
        result = []
        for i in range(instruments.shape[0]):
            trade_dts = calendars[calendars[0] >= self.start_dt]
            trade_dts = trade_dts[trade_dts[0] <= self.end_dt]
            df = trade_dts.reset_index(drop=True)
            df['symbol'] = instruments.loc[i, 'symbol']
            df.rename(columns={0: 'trade_dt'}, inplace=True)
            result.append(df)
        return pd.concat(result, ignore_index=True)

    def id_map_prod(self):
        df = self.wind_cont.copy()
        df = df.reset_index()
        df = df[['futcode', 'contract_id']]
        pattern = r"([a-zA-Z]+)\d"
        df['prod'] = df['futcode'].str.extract(pattern)
        df.drop_duplicates(subset=['contract_id'], inplace=True)
        return df[['contract_id', 'prod']]

    def func_content(self, df):
        df = df.sort_values('trade_dt')
        df['new_content'] = df['new_content'].ffill()
        df['old_content'] = df['old_content'].bfill()
        df['content'] = df.apply(lambda x: x['old_content'] if pd.isna(x['new_content']) else x['new_content'], axis=1)
        return df

    def ext_content(ctx, df):
        pattern = "[0-9]+:[0-9]+"
        df['time'] = df['content'].apply(lambda x: re.findall(pattern, x))
        df['am_start'] = df['time'].apply(lambda x: x[0] if len(x) > 0 else np.nan)
        df['am_end'] = df['time'].apply(lambda x: x[1] if len(x) > 1 else np.nan)
        df['pm_start'] = df['time'].apply(lambda x: x[2] if len(x) > 2 else np.nan)
        df['pm_end'] = df['time'].apply(lambda x: x[3] if len(x) > 3 else np.nan)
        df['night_start'] = df['time'].apply(lambda x: x[4] if len(x) > 4 else np.nan)
        df['night_end'] = df['time'].apply(lambda x: x[5] if len(x) > 5 else np.nan)

    @context_data
    def get_trading_hrs(self):
        prochange = self.wind_cont_chg.copy()
        prochange = prochange[prochange.item == '交易时间'].reset_index()
        # 万得id与品种对应
        wi_map = self.id_map_prod()
        prochange = pd.merge(prochange, wi_map, on='contract_id', how='left')
        prochange = prochange[['prod', 'ann_dt', 'old_content', 'new_content']]
        prochange.rename(columns={'ann_dt': 'date'}, inplace=True)

        ann2trade = ann_map_trade(self.get_calendars())
        prochange = pd.merge(prochange, ann2trade, on='date', how='left')

        full_index = self.get_full_index()
        full_index['prod'] = full_index['symbol'].apply(lambda x: x[2].upper() if x[1] == 'x' else x[1:3].upper())
        trading_hrs = pd.merge(full_index, prochange, on=['prod', 'trade_dt'], how='left')
        # trading_hrs = trading_hrs.groupby('symbol').apply(func_content)
        # trading_hrs = [self.func_content(df) for _, df in trading_hrs.groupby('prod')]
        # trading_hrs = pd.concat(trading_hrs, ignore_index=True)

        tasks = [delayed(self.func_content)(df) for _, df in trading_hrs.groupby('prod')]
        trading_hrs = Parallel(n_jobs=12)(tasks)
        trading_hrs = pd.concat(trading_hrs, ignore_index=True)


        trading_hrs = add_content(self.wind_cont.copy(), trading_hrs)
        self.ext_content(trading_hrs)
        trading_hrs = trading_hrs[['trade_dt', 'symbol', 'content', 'am_start', 'am_end',
                                   'pm_start', 'pm_end', 'night_start', 'night_end']]
        return trading_hrs

    def table_concat(self):
        """三个日行情表合并"""
        df = pd.concat([self.wind_eod_com, self.wind_eod_idx, self.wind_eod_bond], ignore_index=True)
        return df

    def add_multiplier(self, df):
        """添加合约乘数"""
        multiplier = self.wind_cont.reset_index()
        fin_mask = multiplier.exname == 'CFFEX'
        multiplier.loc[fin_mask, 'multiplier'] = multiplier.loc[fin_mask, 'cemultiplier']
        multiplier.loc[~fin_mask, 'multiplier'] = multiplier.loc[~fin_mask, 'punit'] * multiplier.loc[~fin_mask, 'rtd']
        multiplier = multiplier[['futcode', 'multiplier']]
        multiplier = rec_czc_by_delistdate(self.wind_des.copy(), multiplier)
        df = pd.merge(df, multiplier, how='left', on='futcode')
        return df

    def add_margin(self, df):
        """添加保证金"""
        margin = self.wind_margin.reset_index()
        margin = rec_czc_by_delistdate(self.wind_des.copy(), margin)
        df = pd.merge(df, margin, how='left', on=['futcode', 'trade_dt'])
        df['marginratio'].fillna(method='ffill', inplace=True)
        df['marginratio'] = df['marginratio'].astype(float)
        df['margin'] = df['settle'] * df['multiplier'] * df['marginratio'] * df['oi']
        df.drop(['marginratio'], axis=1, inplace=True)
        return df

    def fill_limit(self, df):
        # dataframe向下补数
        df['pct_chg_limit'] = df['pct_chg_limit'].fillna(method='ffill')
        # up down_limit计算
        df['pre_close'] = df['close'].shift(1)
        df['up_limit'] = df['pre_close'] * (1 + df['pct_chg_limit'] / 100)
        df['down_limit'] = df['pre_close'] * (1 - df['pct_chg_limit'] / 100)
        df.drop(['pre_close'], inplace=True, axis=1)
        return df

    def add_limit(self, df):
        df_clim = self.wind_limit.reset_index()
        df_clim = rec_czc_by_delistdate(self.wind_des.copy(), df_clim)
        df_clim.rename(columns={"change_dt": "trade_dt"}, inplace=True)
        df = pd.merge(df, df_clim, how='left', on=['futcode', 'trade_dt'])
        # 向下填充
        df = df.groupby('futcode').apply(self.fill_limit)
        return df

    def add_ctm(self, df):
        instruments = self.get_instruments()
        instruments.columns = ['symbol', 'futcode', 'listdate', 'delistdate']
        df = pd.merge(df, instruments, on='symbol', how='left')
        ann2index = ann_map_trade(self.get_calendars())
        ann2index.set_index('data', inplace=True)
        # cal_ctm
        df['ctm'] = df.apply(lambda x: ann2index.loc[x['delistdate'], 'index'] - ann2index.loc[x['trade_dt'], 'index'],
                             axis=1)
        df.drop(['listdate', 'delistdate'], axis=1, inplace=True)
        return df

    @context_data
    def get_eodprice(self):
        # 获取基础日行情数据
        df = self.table_concat()
        # 根据真实合约筛选(已进行郑商所补齐）
        df = select_by_instrument(self.get_instruments(), df)
        # 合约乘数
        # df = self.add_multiplier(df)
        # 保证金
        # df = self.add_margin(df)
        # 涨跌停
        # df = self.add_limit(df)
        # symbol映射
        update_prod_name(df)
        fut2symbol(df)
        # ctm
        df = self.add_ctm(df)
        return df




















    def init_from_wind(self):
        pass

    @retry(max_attempts=5, delay=1)
    def to_feature(self, ds, feature_name, database=None, des=''):
        """
            将df转换为非结构化数据
        """
        if database is None:
            database = self.user_db_name
        print(f'writing {feature_name}')
        idx_names = ds.index.names
        df = ds.reset_index().rename(columns={0: 'value'})
        df['feature'] = feature_name
        df.drop_duplicates(subset=idx_names, inplace=True)
        self.to_parquet(database + '.feature', df, partition_by=['feature'])

        # json_file =  os.path.join(self.user_save_path, database, 'feature', f'feature={feature_name}', 'des.json' )
        # metadata = {}
        # metadata['primary_keys'] = idx_names
        # metadata['des'] = des
        # metadata['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # write_json(metadata, json_file)

    def is_tds(self, dts: np.ndarray, exclude=(0, 99999999)):
        """是否日期序列均为交易日"""
        exclude_mask = np.isin(dts, exclude)
        return np.isin(dts[~exclude_mask], self.cn_tds).all()

    def cal2td(self, dts):
        """ 日历日期转换为trade dt """
        return self.trade_dts[self.dt_loc(dts)]

    def isin_instrument(self, stklist):
        """ 是否在股票池中 """
        return np.isin(stklist, self.instruments)

    def pivot_dup(self, df, aggfunc='sum'):
        """ pivot: with duplicates """
        df['trade_dt'] = self.cal2td(df['trade_dt'])
        name = df.columns.drop(['stockcode', 'trade_dt'])[0]
        ndns_df = df.pivot_table(index='trade_dt', columns='stockcode', values=name, aggfunc=aggfunc) \
            .reindex(index=self.trade_dts, columns=self.instruments)
        return ndns_df

    def shift_tds(self, dts, n):
        """把日期变成，前后n个交易日， n不能为0
        n = -1： 向前找最近的一个交易日，
        n = 0： 向后找最近的一个交易日
        如果不在交易日为首日 越界返回0和99999999
        np.searchsorted会找到最近日期靠后的一天的位置
        """
        dts = dts.values
        tds = self.cn_tds.copy()
        loc = np.searchsorted(tds, dts) + n
        overupper = loc > len(tds) - 1
        belowlower = loc < 0
        normal = ~(overupper | belowlower)

        result = np.ones_like(dts)
        result[normal] = tds[loc[normal]]
        result[overupper] = 99999999
        result[belowlower] = 0
        return result

    def get_univ(self, df, right_close=True):
        """ df中包含stockcode, indate, outdate; 日期nan的位置填充9999999
        right_close: outdate是否是右闭的
        """
        assert (np.isin(['stockcode', 'indate', 'outdate'], df.columns).all())
        if not right_close:
            df['outdate'] = self.shift_tds(df['outdate'], -1)
            assert (self.is_tds(df['outdate']))
        else:
            assert (self.is_tds(df['outdate']))
        df.indate = df.indate.clip(lower=self.trade_dts[0])
        df.outdate = df.outdate.clip(upper=self.trade_dts[-1])
        df = df[df['outdate'] >= df['indate']]
        df = df[self.isin_instrument(df['stockcode'])]  # 退市后依旧在

        indate_df = df[['stockcode', 'indate']].rename(columns={'indate': 'trade_dt'})
        indate_df['value'] = 1.0
        indate_mat = self.pivot_dup(indate_df)
        outdate_df = df[['stockcode', 'outdate']].rename(columns={'outdate': 'trade_dt'})
        outdate_df['value'] = 1.0
        outdate_mat = self.pivot_dup(outdate_df)
        indate_mat.fillna(0, inplace=True)
        outdate_mat.fillna(0, inplace=True)

        result = indate_mat.cumsum() - outdate_mat.cumsum()
        result += outdate_mat

        result.replace(0, np.nan, inplace=True)
        result[result > 0] = 1.0
        return result

    def dt_loc(self, dts):
        """ 获取 dts 在 trade_dts 上的位置，如果找不到取后值位置
        nan的位置变nan
        """
        loc = np.searchsorted(self.trade_dts, dts)
        return np.clip(loc, a_min=0, a_max=self.nd - 1)

    def stk_loc(self, stks):
        """返回instrument上门的排序"""
        return self.ns_dict[stks].values

    def get_ind(self, df, on):
        """ 生成ndns的行业分类要求字段：['ind', 'stockcode', 'indate', 'outdate'];都是右闭 """
        assert (np.isin(['stockcode', 'indate', 'outdate'], df.columns).all())
        df = df[['stockcode', 'indate', 'outdate', on]].rename(columns={on: 'ind'})

        df.indate = df.indate.clip(lower=self.trade_dts[0])
        df.outdate = df.outdate.clip(upper=self.trade_dts[-1])
        df = df[df['outdate'] >= df['indate']]
        df = df[self.isin_instrument(df['stockcode'])]
        inds = np.unique(df['ind'])
        indmap = pd.Series(np.arange(len(inds)), index=inds)

        df['indate_loc'] = self.dt_loc(df['indate'])
        df['outdate_loc'] = self.dt_loc(df['outdate'])
        df['stk_loc'] = self.stk_loc(df['stockcode'])
        df['weight'] = df['ind'].replace(indmap)

        result = np.empty([self.nd, self.ns]) * np.nan
        for i_row, row in df.iterrows():
            mat_i = np.arange(row['indate_loc'], row['outdate_loc'] + 1)  # 右闭
            mat_j = [int(row['stk_loc'])]
            idx = np.ix_(mat_i, mat_j)
            result[idx] = row['weight']
        ndns_df = pd.DataFrame(result, index=self.trade_dts, columns=self.instruments)
        return ndns_df

    def to_ndns(self, ds, ndns_sorted=True):
        """ ds: with ndnp_idx 变成ndns_df
        ndns_sorted: False: 代表ndns有序
        """
        # name = ds.name
        assert (isinstance(ds, pd.Series))
        if ndns_sorted:
            assert (ds.index.names == self.ndns_pkeys)
            v = ds.values.reshape([self.ns, self.nd]).T
            result = pd.DataFrame(v, index=self.trade_dts, columns=self.instruments)
        else:
            result = ds.unstack(level=0).reindex(index=self.trade_dts, columns=self.instruments)
        return result

    def to_nans(self, ds, nans_sorted=True):
        """ ds: with ndnp_idx 变成ndns_df
        ndns_sorted: True: 代表nans有序
        """
        # name = ds.name
        assert (isinstance(ds, pd.Series))
        if nans_sorted:
            assert (ds.index.names == self.nans_pkeys)
            v = ds.values.reshape([self.ns, self.na]).T
            result = pd.DataFrame(v, index=self.ann_dts, columns=self.instruments)
        else:
            result = ds.unstack(level=0).reindex(index=self.ann_dts, columns=self.instruments)
        return result

    def run(self, file):
        """run cscdata init first, then use func to init here params"""
        super().run(file)

        self.init_from_wind()


        # 必须传入的配置时间轴，为取历史数据使用
        localdata.initialize(self.trade_dts)

        # users func
        self._on("_init")
