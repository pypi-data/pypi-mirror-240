# -*- coding:utf-8 _*-

import pandas as pd
import concurrent
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

doc = \
    '''
	此表包含ndns轴的所有基础数据， 各种univ和barra等
'''
# from ..utils.logger import gen_log

# log = gen_log(r"K:\cscfut\cscquant\test\log")

import sys
sys.path.append(r"K:\cscfut\work_rp")

import numpy as np
# from work_rp.context_ import FinContext
from cscdata.localdata.stock.context_stk import FinContext
from cscdata.localdata.stock.lib import CiticsInd
from functools import lru_cache
import warnings
warnings.filterwarnings('ignore')

@lru_cache
def univ_st(ctx):
    '''ST股票univ'''
    df = ctx.ds('asharest').get_df(index = False)
    df.rename(columns={'entry_dt': 'indate', 'remove_dt': 'outdate'}, inplace=True)
    ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=False)
    ndns_df = ndns_df * ctx.univ_ipo
    return ndns_df


@lru_cache
def univ_ipo60(ctx):
    '''所有上市交易60天后的股票univ'''
    df = ctx.wind_des.copy()
    df['list_dt'] = ctx.shift_tds(df.list_dt, 60)
    df.rename(columns={'list_dt': 'indate', 'delist_dt': 'outdate'}, inplace=True)
    ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=False)
    return ndns_df


@lru_cache
def univ_sus(ctx):
    '''sus:停牌至少一天的univ'''
    df = ctx.ds('ashareeodprices').get_df()
    df['tradestatus'] = (df.tradestatus == '停牌') * 1
    ds = df['tradestatus']
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    ndns_df.replace(0, np.nan, inplace=True)
    return ndns_df


@lru_cache
def univ_updn_bounded(ctx):
    '''可以交易股票集：ipo60天， 非st， 非停牌'''
    df = ctx.ds('zxjtashareeodprices').get_df(['high', 'low', 'upperlimit', 'lowerlimit'])
    up = (df.upperlimit / df.low - 1).abs() < 0.005  #upperlimit ???
    dn = (df.high / df.lowerlimit - 1).abs() < 0.005
    df['value'] = (up | dn).astype(float)
    df.loc[df.value == 0, ("value",)] = np.nan
    ndns_df = ctx.to_ndns(df.value, ndns_sorted=False)
    return ndns_df


@lru_cache
def univ_tradable(ctx):
    '''可以交易股票集：ipo60天， 非停牌, 非一字涨跌停'''
    ndns_df = univ_ipo60(ctx).copy()
    ndns_df[univ_sus(ctx) == 1.0] = np.nan
    ndns_df[univ_updn_bounded(ctx) == 1.0] = np.nan
    return ndns_df


@lru_cache
def univ_all(ctx):
    univ = ((univ_ipo60(ctx) == 1) & (univ_st(ctx) != 1) & (univ_sus(ctx) != 1)).astype(float)
    univ[univ == 0] = np.nan
    return univ


@lru_cache
def ndns_ret(ctx):
    '''股票涨跌幅（不复权）'''
    df = ctx.ds('ashareeodprices').get_df()
    df['ret'] = (df['adjclose'] - df['adjpreclose']) / df['adjpreclose']
    ds = df['ret']
    ndns_df = ctx.to_ndns(ds, False)
    return ndns_df


@lru_cache
def ndns_pctchange(ctx):
    '''股票涨跌幅（复权）， 不带分红'''
    ds = ctx.ds('ashareeodprices').get_df('pctchange')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_adjclose(ctx):
    '''股票复权close'''
    ds = ctx.ds('ashareeodprices').get_df('adjclose')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_close(ctx):
    '''股票收盘价'''
    ds = ctx.ds('ashareeodprices').get_df('close')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_amount(ctx):
    '''股票收盘价'''
    ds = ctx.ds('ashareeodprices').get_df('amount')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_volume(ctx):
    '''交易量'''
    ds = ctx.ds('ashareeodprices').get_df('volume')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_adv20(ctx):
    '''过去20天平均交易额median'''
    ds = ctx.ds('ashareeodprices').get_df('amount')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df.rolling(20).sum()


@lru_cache
def ndns_adv40(ctx):
    '''过去20天平均交易额median'''
    ds = ctx.ds('ashareeodprices').get_df('amount')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df.rolling(40).sum() # sum?   not  mean?


@lru_cache
def ndns_totmv(ctx):
    '''股票总市值'''
    ds = ctx.ds('ashareeodderivativeindicator').get_df('tot_mv')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_dqmv(ctx):
    '''股票流通市值'''
    ds = ctx.ds('ashareeodderivativeindicator').get_df('dq_mv')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_freemv(ctx):
    '''股票自由流通市值'''
    df = ctx.ds('ashareeodderivativeindicator')[['close', 'free_shr']]
    df['freemv'] = df['close'] * df['free_shr']
    ndns_df = ctx.to_ndns(df['freemv'], False)
    return ndns_df


@lru_cache
def ndns_totshr(ctx):
    '''股票总股本'''
    ds = ctx.ds('ashareeodderivativeindicator').get_df('tot_shr')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_dqshr(ctx):
    '''股票流通股本'''
    ds = ctx.ds('ashareeodderivativeindicator').get_df('dq_shr')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_freeshr(ctx):
    '''股票自由流通股本'''
    ds = ctx.ds('ashareeodderivativeindicator').get_df('free_shr')
    ndns_df = ctx.to_ndns(ds, ndns_sorted=False)
    return ndns_df


@lru_cache
def ndns_tvr(ctx):
    '''流通市值换手率（默认）：amt/；流通市值'''
    # ndns_df = ndns_volume(ctx)/ndns_dqshr(ctx)
    # 和ashareeodderivativeindicator表中的换手比对, 进行检查
    ds = ctx.ds('ashareeodderivativeindicator')['dq_turnover']
    ndns_df = ctx.to_ndns(ds, False)
    return ndns_df


@lru_cache
def ndns_tvrtot(ctx):
    '''总市值换手率：amt/总市值'''
    ndns_df = ndns_volume(ctx) / ndns_totshr(ctx)
    return ndns_df


@lru_cache
def ndns_tvrfree(ctx):
    '''自由流通换手率：amt/自由流通市值'''
    ndns_df = ndns_volume(ctx) / ndns_freeshr(ctx)
    return ndns_df


@lru_cache
def univ_zz500(ctx):
    '''A股 tradable 中证500'''
    df = ctx.ds('aindexmembers').get_df(index=False)
    df = df[df.indexcode == '000905.SH']
    ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=True)
    ndns_df = ndns_df * univ_all(ctx)
    # (bbdata('univ_mask_zz500').fillna(0) == ndns_df.fillna(0)).all().all()
    # np.where(bbdata('univ_mask_zz500').fillna(0) != ndns_df.fillna(0))
    return ndns_df


@lru_cache
def univ_hs300(ctx):
    '''A股 tradable 沪深300'''
    df = ctx.ds('aindexmembers').get_df(index=False)
    df = df[df.indexcode == '000300.SH']
    ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=True)
    ndns_df = ndns_df * univ_all(ctx)
    # from BBData import D
    # wcc_sus = D.features_mmat('univ_mask_hs300', start_time=20070101, end_time=20211231)['univ_mask_hs300']
    # (wcc_sus.fillna(0) == ndns_df.fillna(0)).all().all()
    # np.where(wcc_sus.fillna(0) != ndns_df.fillna(0))
    return ndns_df


@lru_cache
def univ_zz1000(ctx):
    '''A股 tradable 中证1000'''
    df = ctx.ds('aindexmembers').get_df(index=False)
    df = df[df.indexcode == '000852.SH']
    ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=True)
    ndns_df = ndns_df * univ_all(ctx)
    return ndns_df


@lru_cache
def univ_zz800(ctx):
    '''A股 tradable 中证800'''
    df = ctx.ds('aindexmembers').get_df(index=False)
    df = df[df.indexcode == '000906.SH']
    ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=True)
    ndns_df = ndns_df * univ_all(ctx)
    return ndns_df


@lru_cache
def univ_zz2000(ctx):
    '''A股 tradable 中证2000'''
    df = ctx.ds('aindexmembers').get_df(index=False)
    df = df[df.indexcode == '932000.CSI']
    ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=True)
    ndns_df = ndns_df * univ_all(ctx)
    return ndns_df


@lru_cache
def univ_top2500(ctx):
    '''A股 tradable top2500'''
    ndns_df = ndns_adv20(ctx).copy()
    ndns_df = ndns_df * univ_all(ctx)
    ndns_df = ndns_df.rank(axis=1, ascending=False)
    ndns_df[ndns_df > 2500] = np.nan
    ndns_df[~ndns_df.isna()] = 1.0
    return ndns_df


@lru_cache
def univ_top70p(ctx):
    '''A股 tradable top 70%'''
    ndns_df = ndns_adv20(ctx).copy()
    ndns_df = ndns_df * univ_all(ctx)
    ndns_df = ndns_df.rank(axis=1, ascending=False)
    ndns_df[ndns_df.ge(round(ndns_df.max(axis=1) * 0.7), axis=0)] = np.nan
    ndns_df[~ndns_df.isna()] = 1.0
    return ndns_df


@lru_cache
def ind_citics1(ctx):
    '''中信一级分类'''
    ci = CiticsInd(ctx)
    ndns_df = ci.get_ndns(1)
    # (bbdata('ndns_indu').fillna(0) == ndns_df.fillna(0)).all().all()
    return ndns_df


@lru_cache
def ind_citics2(ctx):
    '''中信二级分类'''
    ci = CiticsInd(ctx)
    return ci.get_ndns(2)


@lru_cache
def ind_citics3(ctx):
    '''中信三级分类'''
    ci = CiticsInd(ctx)
    return ci.get_ndns(3)


# def main_threads(parallel=True, max_workers=12):
#     funcs = [
#         'univ_st',
#         'univ_ipo60',
#         'univ_sus',
#         'univ_updn_bounded',
#         'univ_tradable',
#         'univ_all',
#         'ndns_ret',
#         'ndns_pctchange',
#         'ndns_adjclose',
#         'ndns_close',
#         'ndns_amount',
#         'ndns_volume',
#         'ndns_adv20',
#         'ndns_adv40',
#         'ndns_totmv',
#         'ndns_dqmv',
#         'ndns_freemv',
#         'ndns_totshr',
#         'ndns_dqshr',
#         'ndns_freeshr',
#         'ndns_tvr',
#         'ndns_tvrtot',
#         'ndns_tvrfree',
#         'univ_zz500',
#         'univ_hs300',
#         'univ_zz1000',
#         'univ_zz800',
#         'univ_top2500',
#         'univ_top70p',
#         'ind_citics1',
#         'ind_citics2',
#         'ind_citics3',
#     ]
#     ctx = FinContext()
#
#     def worker(func_name):
#         print(f'processing... {func_name}')
#         func = eval(func_name)
#         data = func(ctx)
#         ctx.to_feature(data.stack(), func_name, des=func.__doc__)
#         return func_name
#
#     if parallel:
#         with ThreadPoolExecutor(max_workers=max_workers) as executor:
#             futures = [executor.submit(worker, func_name) for func_name in funcs]
#         # 处理并打印结果
#         for future in concurrent.futures.as_completed(futures):
#             print(f"{future.result()} saved and completed")
#     else:
#         for func_name in funcs:
#             worker(func_name)
#             print(f"{func_name} saved and completed")

def read(ctx):
    return ctx.uds("rp.feature.feature=univ_st").get_df()

# def worker(ctx,func_name):
#     print(func_name)
#     df = read(ctx)
#     print(df.head())

def worker(ctx, func_name):
    print(f'processing... {func_name}')
    func = eval(func_name)
    data = func(ctx)
    ctx.to_feature(data.stack(), func_name, des=func.__doc__)
    return func_name

def on_init(ctx):
    task_list = [
    'univ_st',
    'univ_ipo60',
    # 'univ_sus',
    # 'univ_updn_bound',
    # 'univ_tradable',
    # 'univ_all',
    # 'ndns_ret',
    # 'ndns_pctchange'
    # 'ndns_adjclose',
    # 'ndns_close',
    # 'ndns_amount',
    # 'ndns_volume',
    # 'ndns_adv20',
    # 'ndns_adv40',
    # 'ndns_totmv',
    # 'ndns_dqmv',
    # 'ndns_freemv',
    # 'ndns_totshr',
    # 'ndns_dqshr',
    # 'ndns_freeshr',
    # 'ndns_tvr',
    # 'ndns_tvrtot',
    # 'ndns_tvrfree',
    # 'univ_zz500',
    # 'univ_hs300',
    # 'univ_zz1000',
    # 'univ_zz800',
    # 'univ_top2500',
    # 'univ_top70p',
    # 'ind_citics1',
    # 'ind_citics2',
    # 'ind_citics3',
]
    for func in task_list:
        worker(ctx, func)
        # df = univ_hs300(ctx)

def on_ann_dt(ctx):
    pass

def on_trade_dt(ctx):
    pass

__config__ = {
    "cscdata_init_repo": r"Q:\data_to_now",
    "db_name": 'dsets',
    "user_repo": r"K:\qtData\cscdata_repo",
    "user_db_name": 'xhn'
}

# if __name__ == '__main__':
#     # ctx = FinContext()
#     log.info('start to base ndns')
#     main_threads()
#     log.info('finish building base ndns')
#     # ind_citics3(ctx)

if __name__ == '__main__':
    ctx = FinContext()
    ctx.run(__file__)
