import json
from collections import defaultdict
import numpy as np
from cfg import *
import pandas as pd


def rec_czc_by_delistdate(des, df):
    df = pd.merge(df, des[['futcode', 'delist_dt']], on='futcode', how='left')
    df['futcode'] = df.apply(lambda x: x['futcode'][:-7] + str(x['delist_dt'])[2] + x['futcode'][-7:] if (
            x['futcode'][-3:] == 'CZC' and 'A' <= x['futcode'][-8] <= 'Z') else x['futcode'], axis=1)
    df.drop(['delist_dt'], axis=1, inplace=True)
    return df


def rec_czc_by_tradedate(df):
    df['f'] = df.apply(lambda x: (x['trade_dt'] // 100000) % 10 + 1 if x['futcode'][-3:] == 'CZC' and int(
        x['futcode'][-7]) < (x['trade_dt'] // 10000) % 10 else (x['trade_dt'] // 100000) % 10, axis=1)
    df['futcode'] = df.apply(lambda x: x['futcode'][:-7] + str(x['f']) + x['futcode'][-7:] if (
            x['futcode'][-3:] == 'CZC' and 'A' <= x['futcode'][-8] <= 'Z') else x['futcode'], axis=1)
    df.drop(['f'], axis=1, inplace=True)
    # update_prod_name(df)


def select_by_instrument(contracts, df):
    """根据合约池筛选(必要原则是统一名称和长度字段，因为这些很难逆向还原)"""
    df = df[df.futcode.map(lambda x: len(x) >= 8)]
    df = df[~(df.type == '1')]
    df = df[~(df.type == '3')]
    # 删除无意义column
    df.drop(['type', 'cccode'], axis=1, inplace=True)
    rec_czc_by_tradedate(df)
    # 根据当前合约筛选
    contracts = contracts['futcode'].to_numpy()
    df = df[df['futcode'].isin(contracts)]
    return df


def add_content(pro, df):
    """对于从未更改的进行补足"""
    pro = pro[['prod_code', 'thours', 'contract_id']]
    pro = pro.drop_duplicates(subset=['contract_id'], keep='last')
    pro.rename(columns={'prod_code': 'prod'}, inplace=True)
    df = pd.merge(df, pro, on='prod', how='left')
    df['content'] = df.apply(lambda x: x['thours'] if pd.isna(x['content']) else x['content'], axis=1)
    return df


def ann_map_trade(trade_dts):
    trade2index = trade_dts.reset_index()
    trade2index.columns = ['index', 'date']
    ann_date = pd.date_range(str(trade2index['date'].min()), str(trade2index['date'].max()))
    ann_date = ann_date.astype(str).to_numpy()
    ann2trade = pd.DataFrame(columns=['date'], data=ann_date)
    ann2trade['date'] = ann2trade['date'].apply(lambda x: int(x[:4]+x[5:7]+x[8:]))
    ann2trade = pd.merge(ann2trade, trade2index, on='date', how='left')
    ann2trade = ann2trade.fillna(method='bfill')
    date = trade2index['date'].to_numpy()
    ann2trade['trade_dt'] = ann2trade.apply(lambda x: date[int(x['index'])], axis=1)
    return ann2trade[['date', 'trade_dt', 'index']]


def check_prod_name():
    with open(r'K:\qtData\futdata\products.json', 'r', errors='ignore') as f:
        content = json.load(f)
    new_map_old = defaultdict(list)
    old_map_old = defaultdict(list)
    for c in content:
        if c['old_code']:
            new_map_old[c['code'].upper()] = c['old_code'].upper()
            old_map_old[c['old_code'].upper()] = c['code'].upper()


def check_contract(cur_contract):
    """判定是否含有新增,如果有则输出(这里默认了内容只增不减)"""
    his_contract = np.loadtxt(save_path+'/instruments/contract.txt', delimiter=',', dtype=str)
    num = cur_contract.shape[0]-his_contract.shape[0]
    if num == 0:
        print('no new product')
    else:
        new_contract = list(cur_contract.iloc[-num:, 0])
        print('new products numbers:', num)
        print('，'.join(i for i in new_contract))


def select_contract(df):
    # 根据合约类型筛选真实合约（月合约）
    df = df[df.contract_type == 1]
    # 筛选命名(含_ -和tas）
    df = df[~(df.futcode.str.contains('-') | df.futcode.str.contains('_') | df.futcode.str.contains('TAS'))]
    # 筛选仿真合约
    pattern = r"([a-zA-Z]+)\d"
    df['prod'] = df['futcode'].str.extract(pattern)
    df = df[df["prod"].map(lambda x: len(x) < 3)].reset_index(drop=True)
    return df


def rec_czc(df):
    df['futcode'] = df.apply(lambda x: x['futcode'][:-7] + str(x['delist_dt'])[2] + x['futcode'][-7:] if (
            x['futcode'][-3:] == 'CZC' and 'A' <= x['futcode'][-8] <= 'Z') else x['futcode'], axis=1)


def rec_czc_by_trade_dt(df):
    df['de'] = df.apply(
        lambda x: (x['trade_dt'] // 100000) % 10 + 1 if int(x['futcode'][2]) < (x['trade_dt'] // 10000) % 10 \
            else (x['trade_dt'] // 100000) % 10, axis=1)
    df['futcode'] = df.apply(lambda x: x['futcode'][:-7] + str(x['de']) + x['futcode'][-7:] \
        if (x['futcode'][-3:] == 'CZC' and 'A' <= x['futcode'][-8] <= 'Z') else x['futcode'], axis=1)
    df.drop(['de'], axis=1, inplace=True)


def symbol2fut(contract):
    f = np.frompyfunc(lambda x: x[2:].upper()+'.'+exch_l2u[x[0]] if x[1] == 'x' else x[1:].upper()+'.'+exch_l2u[
        x[0]], 1, 1)
    return f(contract)


def update_prod_name(df):
    # 品种名修订为最新的
    map_prod_name = gen_name_map()
    df['symbol'] = df['futcode'].apply(lambda x: map_prod_name[x[:-8]] + x[-8:] if map_prod_name[x[:-8]] else x)


def fut2symbol(df):
    """将标准后的futcode转化为统一的symbol"""
    df['symbol'] = df['symbol'].apply(lambda x: (exch_u2l[x[-3:]] + x[:-4]).lower() if 'A' <= x[1] <= 'Z' else (
            exch_u2l[x[-3:]] + 'x' + x[:-4]).lower())


def wind2symbol(df):
    # 郑商所日期补全
    rec_czc(df)
    # 品种名修订为最新的
    update_prod_name(df)
    # 转化为symbol
    fut2symbol(df)


if __name__ == '__main__':
    pass
