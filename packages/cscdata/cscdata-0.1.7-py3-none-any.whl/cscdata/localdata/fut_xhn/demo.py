import numpy as np
from context import FuntContext
from functools import lru_cache
import warnings
warnings.filterwarnings('ignore')

# @lru_cache
# def univ_st(ctx):
#     '''ST股票univ'''
#     df = ctx.ds('asharest').get_df(index = False)
#     df.rename(columns={'entry_dt': 'indate', 'remove_dt': 'outdate'}, inplace=True)
#     ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=False)
#     ndns_df = ndns_df * ctx.univ_ipo
#     return ndns_df
#
#
# @lru_cache
# def univ_ipo60(ctx):
#     '''所有上市交易60天后的股票univ'''
#     df = ctx.wind_des.copy()
#     df['list_dt'] = ctx.shift_tds(df.list_dt, 60)
#     df.rename(columns={'list_dt': 'indate', 'delist_dt': 'outdate'}, inplace=True)
#     ndns_df = ctx.get_univ(df[['stockcode', 'indate', 'outdate']], right_close=False)
#     return ndns_df
#
#
# def read(ctx):
#     return ctx.uds("rp.feature.feature=univ_st").get_df()


# def worker(ctx, func_name):
#     print(f'processing... {func_name}')
#     func = eval(func_name)
#     data = func(ctx)
#     ctx.to_feature(data.stack(), func_name, des=func.__doc__)
#     return func_name


def on_init(ctx):
    instruments = ctx.get_eodprice()
    a = ctx.for_debug()

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


if __name__ == '__main__':
    ctx = FuntContext()
    ctx.run(__file__)
