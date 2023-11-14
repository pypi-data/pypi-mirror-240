# -*- coding:utf-8 -*-
from collections import defaultdict
data_path = r'Q:\data_to_now\dsets'
save_path = r'K:\qtData\futdata'

exch_l2u = {'f': 'CFE', 'c': 'CZC', 'd': 'DCE', 'g': 'GFE', 'i': 'INE', 's': 'SHF'}
exch_u2l = {'CFE': 'f', 'CZC': 'c', 'DCE': 'd', 'GFE': 'g', 'INE': 'i', 'SHF': 's'}
# map_prod_name = {'WH': 'WS', 'PM': 'WT', 'OI': 'RO', 'RI': 'ER', 'MA': 'ME', 'ZC': 'TC'}
map_prod_name_base = {'WS': 'WH', 'WT': 'PM', 'RO': 'OI', 'ER': 'RI', 'ME': 'MA', 'TC': 'ZC'}
def gen_name_map():
    map_prod_name = defaultdict(list)
    for k,v in map_prod_name_base.items():
        map_prod_name[k] = v
    return map_prod_name


