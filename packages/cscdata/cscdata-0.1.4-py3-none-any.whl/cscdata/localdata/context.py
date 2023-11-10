# -*- coding:utf-8 -*-

"""
This module is used to store the context of the whole project
"""

import cscdata.localdata as localdata
# cscdata.init(r"Q:\data_to_now") # dsets\asharecalendar.parquet
import cscdata.localdata.localInit as cli

from .utils import retry

from functools import cached_property
import pandas as pd
import os
import numpy as np
from datetime import datetime

def initialize(trade_dts):
    localdata.initialize(trade_dts)


class QtCalendar:
    ''' 保存所有交易日相关的函数 '''
    def __init__(self, trade_dts_df, all_dts: np.ndarray = None):
        if all_dts is None:
            df = trade_dts_df
            self.all_dts = df.loc['SZSE']['trade_dt'].sort_values().values.astype(int)
        else:
            self.all_dts = all_dts.astype(int)
        self.tds_dict = pd.Series(np.arange(len(self.all_dts)), index=self.all_dts)

    def get_wind_tds(self):
        pass

    def get_trade_dts(self, start_dt, end_dt):
        return self.all_dts[(self.all_dts >= start_dt) & (self.all_dts <= end_dt)]

    def get_loc(self, dts):
        ''' is_tds：保证都是交易日 '''
        # result = np.vectorize(self.tds_dict.get)(dts)
        result = np.searchsorted(self.all_dts, dts)
        return np.clip(result, a_min=0, a_max=len(self.all_dts) - 1)

    def shift_tds(self, dts, lag: int):
        ''' 把交易日后移动  -1 代表上一个交易日, -2 代表前两个交易日
        dts: list, scalar or ndarray
        '''
        loc = self.get_loc(dts) + lag
        return self.all_dts[loc]

    def isin_tds(self, dts):
        ''' 是否是交易日 '''
        return np.isin(dts, self.all_dts)

class FinContext:
    def __init__(self, start_dt=20070101, end_dt=20211231, source = 'wind'):
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.source = source

        # init dataapi of localdata
        self.db_name = None
        self.con = None
        self.user_save_path = None
        self.cscdata_init_path = None

        self.callib = None
        self.all_dts = None  # 1990年以来所有的日历日   # v1.4
        self.cn_tds = None  # 1990年以来过去未来全部交易日
        self.ann_dts = None  # [start_dt, end_dt]之间的所有日期日
        self.trade_dts = None  # [start_dt, end_dt]之间的所有交易日
        self.instruments = None  # [start_dt, end_dt]之间的所有上市股票
        self.report_periods = None  # [start_dt, end_dt]外推所有报告期（季度）; 外推3年
        self.report_years = None  # [start_dt, end_dt]外推所有年度报告期

        self.na = 0  # num of 日历日
        self.nd = 0  # num of 交易日
        self.ns = 0  # num of 股票数量
        self.nq = 0  # num of ann_dts

        self.nd_dict = None  # trade_dts反查表
        self.na_dict = None  # ann_dts反查表
        self.ns_dict = None  # instruments反查表
        self.nq_dict = None  # report_periods反查表

        # self.run(file)

        # if source == 'wind':
        #     self.init_from_wind()

        self.ndns_pkeys = ['stockcode', 'trade_dt']
        self.nans_pkeys = ['stockcode', 'ann_dt']
        self.nansnq_pkeys = ['stockcode', 'ann_dt', 'report_period']

        self.ndx_idx = None
        self.univ_ipo = None
        self.nans_ipo = None
        self.nans_idx = None

        # init params
        # self.trade_dts = self.get_trade_dts()


    def get_univ_ipo_mat(self):
        ''' univ_ipo to ndns_df  上市股票全集'''
        result = self.to_ndns(self.ndns_idx['univ_ipo'], ndns_sorted=False)
        return result

    def get_univ_ipo(self):
        '''获取ndns轴， 添加listed'''
        df = self.wind_des.copy()
        df.rename(columns={'list_dt': 'indate', 'delist_dt': 'outdate'}, inplace=True)
        ndns_df = self.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=False)
        result = pd.DataFrame({'univ_ipo': ndns_df.unstack(level=1)})
        return result

    @cached_property
    def wind_cal(self):
        return self.ds('asharecalendar').get_df(index=False)

    @cached_property
    def wind_des(self):
        return self.ds('asharedescription').get_df(index=False)

    def get_instruments(self, start_dt, end_dt):
        ''' 区间内上市的股票 '''
        df = self.wind_des
        return df[(df.delist_dt >= start_dt) & (df.list_dt <= end_dt)].stockcode.values

    def init_from_wind(self):
        # self.db.list_tables()
        df = self.wind_cal
        self.cn_tds = df.loc[df.exch == 'SSE'].sort_values('trade_dt')['trade_dt'].values
        self.callib = QtCalendar(self.wind_cal, all_dts=self.cn_tds)
        self.trade_dts = self.callib.get_trade_dts(self.start_dt, self.end_dt)
        self.instruments = self.get_instruments(self.start_dt, self.end_dt)
        end = self.end_dt + 30000
        rps = pd.date_range(str(self.start_dt), str(end), freq='Q-DEC')  # 外推3年 用于存预期数据
        rys = pd.date_range(str(self.start_dt), str(end), freq='Y')
        self.all_dts = pd.date_range('19900101', str(self.end_dt)).strftime("%Y%m%d").astype(int).values  # v1.4
        self.report_periods = rps.strftime("%Y%m%d").astype(int).values
        self.report_years = rys.strftime("%Y").astype(int).values
        self.ann_dts = pd.date_range(str(self.start_dt), str(self.end_dt)).strftime("%Y%m%d").astype(int).values
        self.nd, self.ns, self.nq, self.na = len(self.trade_dts), len(self.instruments), len(self.report_periods), len(
            self.ann_dts)
        self.nd_dict = pd.Series(np.arange(self.nd), self.trade_dts)
        self.ns_dict = pd.Series(np.arange(self.ns), self.instruments)
        self.nq_dict = pd.Series(np.arange(self.nq), self.report_periods)
        self.na_dict = pd.Series(np.arange(self.na), self.ann_dts)
        self.na_dict1 = pd.Series(np.arange(len(self.all_dts)), self.all_dts)  # v1.4

    # def get_trade_dts(self):
    #     """ get all trade dates """
    #     # if os.name == 'nt':
    #     #     cal_path = r"K:\cscfut\cscquant\utils\asharecalendar.parquet"
    #     # elif os.name == "posix":
    #     #     cal_path = "/mnt/k/cscfut/cscquant/utils/asharecalendar.parquet"
    #     # df = pd.read_parquet(cal_path)
    #     # trade_dts = list(df['trade_dt'].unique())
    #     trade_dts = list(np.load("trade_dts.npy"))
    #
    #     trade_dts = [_td for _td in trade_dts if _td > self.start_dt and _td < self.end_dt]
    #     return trade_dts

    @retry(max_attempts=5, delay=1)
    def to_feature(self, ds, feature_name, des=''):
        """
            将df转换为非结构化数据
        """
        print(f'writing {feature_name}')
        idx_names = ds.index.names
        df = ds.reset_index().rename(columns={0: 'value'})
        df['feature'] = feature_name
        df.drop_duplicates(subset=idx_names, inplace=True)
        self.to_parquet('rp.feature', df, partition_by=['feature'])
        # df.to_parquet(cache_url.features_url, engine='fastparquet', partition_cols='feature', compression='LZ4')

        # json_file = os.path.join()
        # json_file = Path(cache_url.features_url) / f'feature={feature_name}' / f'des.json'
        # metadata = {}
        # metadata['primary_keys'] = idx_names
        # metadata['des'] = des
        # metadata['last_update'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # write_json(metadata, json_file)

    def is_tds(self, dts: np.ndarray, exclude=(0, 99999999)):
        '''是否日期序列均为交易日'''
        exclude_mask = np.isin(dts, exclude)
        return np.isin(dts[~exclude_mask], self.cn_tds).all()

    def cal2td(self, dts):
        ''' 日历日期转换为trade dt '''
        return self.trade_dts[self.dt_loc(dts)]

    def isin_instrument(self, stklist):
        ''' 是否在股票池中 '''
        return np.isin(stklist, self.instruments)

    def pivot_dup(self, df, aggfunc='sum'):
        ''' pivot: with duplicates '''
        df['trade_dt'] = self.cal2td(df['trade_dt'])
        name = df.columns.drop(['stockcode', 'trade_dt'])[0]
        ndns_df = df.pivot_table(index='trade_dt', columns='stockcode', values=name, aggfunc=aggfunc) \
            .reindex(index=self.trade_dts, columns=self.instruments)
        return ndns_df

    def shift_tds(self, dts, n):
        '''把日期变成，前后n个交易日， n不能为0
        n = -1： 向前找最近的一个交易日，
        n = 0： 向后找最近的一个交易日
        如果不在交易日为首日 越界返回0和99999999
        np.searchsorted会找到最近日期靠后的一天的位置
        '''
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
        ''' df中包含stockcode, indate, outdate; 日期nan的位置填充9999999
        right_close: outdate是否是右闭的
        '''
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
        ''' 获取 dts 在 trade_dts 上的位置，如果找不到取后值位置
        nan的位置变nan
        '''
        loc = np.searchsorted(self.trade_dts, dts)
        return np.clip(loc, a_min=0, a_max=self.nd - 1)

    def stk_loc(self, stks):
        '''返回instrument上门的排序'''
        return self.ns_dict[stks].values

    def get_ind(self, df, on):
        ''' 生成ndns的行业分类要求字段：['ind', 'stockcode', 'indate', 'outdate'];都是右闭 '''
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
        ''' ds: with ndnp_idx 变成ndns_df
        ndns_sorted: False: 代表ndns有序
        '''
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
        ''' ds: with ndnp_idx 变成ndns_df
        ndns_sorted: True: 代表nans有序
        '''
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
        """ run the whole project """
        namespace = {}
        with open(file, 'r', encoding='utf-8') as f:
            _fcode = f.read()
            exec(_fcode, namespace)

        # __config__
        __config__ = namespace["__config__"]
        self.db_name = __config__["db_name"]
        self.user_save_path = __config__["user_save_repo"]
        self.cscdata_init_path = __config__["cscdate_init_repo"]

        localdata.init(self.cscdata_init_path)
        self.con = cli.DataAPI(self.db_name)

        # init data
        self.init_from_wind()
        self.ndns_idx = self.get_univ_ipo()  # 2.4s

        # 部分ndns数据
        self.univ_ipo = self.get_univ_ipo_mat()
        self.nans_ipo = self.univ_ipo.reindex(index=self.ann_dts)
        self.nans_idx = pd.DataFrame({'univ_ipo': self.nans_ipo.unstack(level=1)})
        self.nans_idx.index = self.nans_idx.index.set_names(self.nans_pkeys)

        initialize(self.trade_dts)

        # __function__
        # exec on_init
        namespace['on_init'](self)

        # run trade_dt
        for trade_dt in self.trade_dts:
            self.cur_trade_dt = trade_dt

            namespace["on_trade_dt"](self)
            self.step()

    def parallel_run(self, file):
        pass

    def step(self):
        """ step forward """
        pass

    def hist(self, table_name, n_day, date_list, columns=None, engine=None):
        """ parquet, get the historical data"""
        return self.ds(table_name).get_hist(n_day, date_list, day_col='trade_dt', columns=columns, engine=engine)

    def parse_dot_name(self, name):
        """parse name as 'a.b', a is db, b is table name"""
        _sp = name.split(".")
        if len(_sp) < 2:
            raise Exception(f"save name '{name}' error, use 'database_name.table_name' ")
        return _sp[0], _sp[1]

    def parse_read_name(self, name):
        """support name """
        _sp = name.split(".")
        if len(_sp) == 1:
            return (name,)
        else:
            return (_sp[0], _sp[1])

    def to_h5(self, name, df, **kwargs):
        """save h5"""
        _db_name, _table_name = self.parse_dot_name(name)
        _db_name = os.path.join(self.user_save_path, _db_name) + '.h5'
        self.con.create_db(_db_name)
        self.con.use_db(_db_name).use_table(_table_name).to_h5(df, **kwargs)

    def to_parquet(self, name, df, partition_by = None, **kwargs):
        """overwrite date to parquet"""
        _db_name, _table_name = self.parse_dot_name(name)
        _db_name = os.path.join(self.user_save_path, _db_name)
        self.con.create_db(_db_name)
        self.con.use_db(_db_name).use_table(_table_name).to_wide_parquet(df, write_mode='w', partition_by = partition_by, **kwargs)

    def insert_h5(self, name, df, **kwargs):
        """insert data to exists h5"""
        self.con.use_table(name).to_h5(df, *kwargs)

    def insert_parquet(self, name, df, **kwargs):
        """insert data to exists parquet"""
        self.con.use_table(name).to_wide_parquet(df, write_mode='a', **kwargs)

    def ds(self, name):
        """ get parquet table """
        name_tuple = self.parse_read_name(name)
        if len(name_tuple) == 1:
            return self.con.use_table(name)
        else:
            _table = self.con.use_db(os.path.join(self.user_save_path, name_tuple[0])).use_table(name_tuple[1])
            self.con.use_db(self.db_name)
            return _table

    def h5(self, name):
        """ get h5 table, by 'h5db_name.table' """
        _db_name, _table_name = self.parse_dot_name(name)
        for _t in os.listdir(localdata.LOCAL_DATA_PATH):
            if _t.startswith(_db_name):
                return self.con.use_db(_db_name).use_table(_table_name)
        raise Exception('read h5 error')

    # def f(self, feature_name):
    #     """ get the feature, feature name like 'table_name.feature'"""
    #     # return Feature(feature_name)
    #     table_name = feature_name.split(".")[0]
    #     fea_name = feature_name.split(".")[1]
    #     table = self.con.use_table(table_name)

    def list_tables(self):
        """ list all tables """
        return self.con.db.show_tables()
