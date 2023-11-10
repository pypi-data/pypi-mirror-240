# -*- coding: utf-8 -*-

import os
from pathlib import Path
from dramkit import isnull
from dramkit import GenObject
from dramkit.iotools import load_yml


FILE_PATH = Path(os.path.realpath(__file__))
ROOT_DIR = str(FILE_PATH.parent.parent).replace('\\', '/')+'/'


# 默认配置文件路径查找顺序，根据需要修改
config_paths = [
    ROOT_DIR + 'finfactory/_config/config.yml',
    'D:/FinFactory/finfactory/_config/config.yml',
    'E:/FinFactory/finfactory/_config/config.yml',
    'F:/FinFactory/finfactory/_config/config.yml',
    'G:/FinFactory/finfactory/_config/config.yml',
    'D:/Genlovy_Hoo/HooProjects/FinFactory/finfactory/_config/config.yml',
    'E:/Genlovy_Hoo/HooProjects/FinFactory/finfactory/_config/config.yml'
    ]

fpath = str(FILE_PATH.parent)
fpath = os.path.join(fpath, '_config', 'config.yml')
config_paths.append(fpath)

cfg_path = None
for fpath in config_paths:
    if os.path.exists(fpath):
        cfg_path = fpath
        break

if not isnull(cfg_path):
    cfg_yml = load_yml(cfg_path, encoding='utf-8')
    cfg = GenObject(**cfg_yml)
else:    
    cfg = GenObject()

# 根据需要修改下面的参数
cfg.set_from_dict(
    {
    # 默认数据存档根目录
    'archive_roots': [
        ROOT_DIR + 'findata/archives/',
        'D:/FinFactory/findata/archives/',
        'E:/FinFactory/findata/archives/',
        'F:/FinFactory/findata/archives/',
        'G:/FinFactory/findata/archives/',
        'D:/Genlovy_Hoo/HooProjects/FinFactory/findata/archives/',
        'E:/Genlovy_Hoo/HooProjects/FinFactory/findata/archives/'
        ],
    
    # 默认日志目录
    'log_dirs': [
        ROOT_DIR + 'fflog/',
        'D:/FinFactory/fflog/',
        'E:/FinFactory/fflog/',
        'F:/FinFactory/fflog/',
        'G:/FinFactory/fflog/',
        'D:/Genlovy_Hoo/HooProjects/FinFactory/fflog/',
        'E:/Genlovy_Hoo/HooProjects/FinFactory/fflog/'
        ],
    
    # 默认因子信息文件路径
    'factors_info_paths': [
        ROOT_DIR + 'finfactory/_config/factors_info.json',
        'D:/FinFactory/finfactory/_config/factors_info.json',
        'E:/FinFactory/finfactory/_config/factors_info.json',
        'F:/FinFactory/finfactory/_config/factors_info.json',
        'G:/FinFactory/finfactory/_config/factors_info.json',
        'D:/Genlovy_Hoo/HooProjects/FinFactory/finfactory/_config/factors_info.json',
        'E:/Genlovy_Hoo/HooProjects/FinFactory/finfactory/_config/factors_info.json'
        ],
        
    # 默认因子数据文件路径
    'factors_data_paths': [
        ROOT_DIR + 'findata/finfactory_factor_data/',
        'D:/FinFactory/findata/finfactory_factor_data/',
        'E:/FinFactory/findata/finfactory_factor_data/',
        'F:/FinFactory/findata/finfactory_factor_data/',
        'G:/FinFactory/findata/finfactory_factor_data/',
        'D:/Genlovy_Hoo/HooProjects/FinFactory/findata/finfactory_factor_data/',
        'E:/Genlovy_Hoo/HooProjects/FinFactory/findata/finfactory_factor_data/'
        ],
    
    'tushare_token_test': 'a09c5fb39f4b5e2a547f1edd31603bd31f2cf9fd50782c964b832f94',
    'gm_token_test': '8532cf7713b1e8a3b7b5ab7b6c8beb6e441845b0',
     
    # 运行Python脚本时是否不保存日志文件
    'no_py_log': True,
    
    # 用ccxt取数据尝试次数和时间间隔（秒）
    'try_get_ccxt': 1,
    'try_get_ccxt_sleep': 10,
    
    # tushare取数尝试次数和间隔时间（秒）
    'try_get_tushare': 1,
    'try_get_tushare_sleep': 10,
    
    # 从财政部网站下载国债和地方债收益率尝试次数和时间间隔（秒）
    'try_get_chn_bond_rates': 2,
    'try_get_chn_bond_rates_sleep': 10,
    
    # 从中金所下载期货龙虎榜数据尝试次数和时间间隔（秒）
    'try_get_cffex': 2,
    'try_get_cffex_sleep': 10,
    
    # 爬取东财数据尝试次数和时间间隔（秒）
    'try_get_eastmoney': 2,
    'try_get_eastmoney_sleep': 10,
    
    # 爬取和讯网数据尝试次数和时间间隔（秒）
    'try_get_hexun': 1,
    'try_get_hexun_sleep': 10,
    
    # 爬取亿牛网数据尝试次数和时间间隔（秒）
    'try_get_eniu': 2,
    'try_get_eniu_sleep': 10,
    
    # 爬取申万数据尝试次数和时间间隔（秒）
    'try_get_sw': 2,
    'try_get_sw_sleep': 10,
    
    # 爬取易方达数据尝试次数和时间间隔（秒）
    'try_get_fundex': 3,
    'try_get_fundex_sleep': 15,
    
    # tushare接口每分钟限制调用次数
    'ts_1min_daily': 400, # 股票日线行情接口
    'ts_1min_daily_basic': 400, # 45 # 股票日线基本数据接口 ***
    'ts_1min_stk_factor': 99, # 股票技术因子接口 ***
    'ts_1min_block_trade': 20, # 大宗交易接口
    'ts_1min_us_tycr': 8, # 美国债收益率接口
    'ts_1min_us_trycr': 8, # 美国债实际收益率接口
    'ts_1min_cctv_news': 5, # 新闻联播文本数接口
    'ts_1min_fut_daily': 15, # 期货日线行情接口
    'ts_1min_fut_mapping': 100, # 主力/连续合约映射接口
    'ts_1min_shibor': 8, # shibo利率接口
    'ts_1min_shibor_lpr': 8, # LPR利率接口
    'ts_1min_opt_daily': 5, # 期权日线接口 ***
    'ts_1min_opt_basic': 5, # 期权合约信息接口 ***
    'ts_1min_top10holders': 300, # 8 # 前十大股东接口 ***
    'ts_1min_top10holders_free': 300, # 8 # 前十大流通股东接口 ***
    'ts_1min_zjc': 250, # 8 # 股东增减持接口 ***
    }
)
