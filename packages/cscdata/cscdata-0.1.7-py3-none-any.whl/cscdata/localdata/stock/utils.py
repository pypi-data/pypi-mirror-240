import pandas as pd
import numpy as np
import json
import random
import os

from functools import wraps
from ..decorators import *

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
    
def LAST_VALID(mat: np.ndarray) -> (np.ndarray, np.ndarray):
    ''' each column 最后一个非nan的位置和值,  如果没有就返回最后一排的值'''
    is_valid = ~np.isnan(mat)
    idxpos = mat.shape[0] - 1 - is_valid[::-1].argmax(0)
    values = mat[idxpos, range(mat.shape[1])]
    return idxpos, values

def write_json(d, file):
    """write json file"""
    with open(file, 'w') as f:
        json.dump(d, f, indent=4)

def read_json(json_file):
    """Read a JSON file and return its content as a Python object."""
    with open(json_file, 'r') as file:
        return json.load(file)

# 只能用在类方法的装饰器
def context_data(func):
    """检查是否已经context.h5中已经有此数据如果存在，则直接读取"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        name = func.__name__
        pth = os.path.join(self.user_repo , self.user_db_name, "stkContext.h5") # users repo
        print(f"context.h5 save path is {pth}")
        while True:
            try:
                f = pd.HDFStore(pth)
                key_existed = name in f
                f.close()
                if os.path.exists(pth) and key_existed:
                    result = pd.read_hdf(pth, name)
                else:
                    result = func(self, *args, **kwargs)
                    result.to_hdf(pth, name)
                break
            except Exception as e:
                print(f" Read context.h5 Error occurred: {e}. Retrying in 1 second...")
                time.sleep(random.random()*2)  # 等待再试
        return result
    return wrapper

