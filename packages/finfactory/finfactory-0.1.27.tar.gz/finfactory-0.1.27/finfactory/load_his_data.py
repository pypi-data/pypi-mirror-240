# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
from pathlib import Path

import struct

from beartype.typing import Union, List

from dramkit import isnull, isna, load_csv, logger_show
from dramkit.iotools import make_dir, load_csvs
from dramkit.gentools import merge_df, check_list_arg
from dramkit.datetimetools import date_reformat
from dramkit.other.othertools import load_text_multi

from finfactory.fintools.utils_chn import get_code_ext
from finfactory.utils.utils import check_date_loss

#%%
FILE_PATH = Path(os.path.realpath(__file__))

TS_NAME_CODE = {
        '上证指数': '000001.SH', 
        '创业板指': '399006.SZ',
        '中小板指': '399005.SZ', 
        '上证50': '000016.SH',
        '沪深300': '000300.SH',
        '中证500': '000905.SH',
        '中证1000': '000852.SH',
        '科创50': '000688.SH',
        '深证成指': '399001.SZ',
    }
for x in ['IF', 'IC', 'IH']:
    TS_NAME_CODE.update({x: x+'.CFX'})
    TS_NAME_CODE.update({x+'9999': x+'.CFX'})
    TS_NAME_CODE.update({x.lower(): x+'.CFX'})
    TS_NAME_CODE.update({x.lower()+'9999': x+'.CFX'})

#%%
class DataArchivesRootDirError(Exception):
    pass


def find_target_dir(dir_name, root_dir=None, make=False,
                    logger=None):
    assert isinstance(root_dir, (type(None), str))
    if isnull(root_dir):
        from finfactory.config import cfg
        prefix_dirs = cfg.archive_roots.copy()
        fpath = str(FILE_PATH.parent.parent)
        fpath = os.path.join(fpath, 'finata', 'archives/')
        fpath = fpath.replace('\\', '/')
        prefix_dirs.append(fpath)
        for dr in prefix_dirs:
            if os.path.exists(dr):
                root_dir = dr
                break
        if isnull(root_dir):
            raise DataArchivesRootDirError(
                '\n未找到按以下顺序的默认数据存档根目录: \n{}'.format(',\n'.join(prefix_dirs)) + \
                ',\n请手动新建或在config.py中配置`archive_roots`！'
                )
    dir_path = root_dir + dir_name
    if not os.path.exists(dir_path):
        if make:
            logger_show('新建文件夹: {}'.format(dir_path),
                        logger, 'info')
            make_dir(dir_path)
            return dir_path
        else:
            raise ValueError('未找到文件夹`{}{}`路径，请检查！'.format(
                             root_dir, dir_name))
    else:
        return dir_path
    
    
def find_paths_year(fpath):
    '''
    根据fpath查找与其相关的带年份后缀的所有路径
    
    TODO: 后缀补位年份时处理（比如后缀为_nan）
    '''
    file = os.path.basename(fpath)
    fdir = str(Path(fpath).parent)
    fdir = fdir.replace('\\', '/')
    tmp = os.listdir(fdir)
    files = []
    for x in tmp:
        x_, type_ = os.path.splitext(x)
        if (x_[:-5]+type_) == file:
            try:
                _ = int(x_[-4:])
                files.append(fdir+'/'+x)
            except:
                pass
    files.sort(key=lambda x: os.path.splitext(x)[0][-4:])
    files.append(fpath)
    return files

#%%
def get_path_ccxt_daily(name1, name2, mkt='binance', root_dir=None):
    fdir = find_target_dir('{}/ccxt_{}/'.format(name1, mkt),
                           root_dir=root_dir)
    fpath = fdir + '{}_daily.csv'.format(name2)
    return fpath


def load_ccxt_daily(name1, name2, mkt='binance', root_dir=None):
    fpath = get_path_ccxt_daily(name1, name2, mkt=mkt, root_dir=root_dir)
    df = load_csv(fpath)
    df['time'] = pd.to_datetime(df['time'])
    # df['time'] = df['time'].apply(lambda x: x-datetime.timedelta(1))
    df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df['date'] = df['time']
    df.sort_values('date', ascending=True, inplace=True)
    df.set_index('date', inplace=True)
    return df


def load_daily_btc126(name1, root_dir=None):
    data_dir = find_target_dir('{}/btc126/'.format(name1),
                               root_dir=root_dir)
    fpaths = [data_dir+x for x in os.listdir(data_dir)]
    data = []
    for fpath in fpaths:
        df = load_csv(fpath)
        data.append(df)
    data = pd.concat(data, axis=0)
    data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'pct%']
    data.sort_values('date', ascending=True, inplace=True)
    data['time'] = data['date'].copy()
    if name1 == 'eth':
        data = data[data['date'] >= '2015-08-07']
    elif name1 == 'btc':
        data = data[data['date'] >= '2010-07-19']
    data.set_index('date', inplace=True)
    data['volume'] = data['volume'].apply(lambda x: eval(''.join(x.split(','))))
    def _get_pct(x):
        try:
            return eval(x.replace('%', ''))
        except:
            return np.nan
    data['pct%'] = data['pct%'].apply(lambda x: _get_pct(x))
    data = data.reindex(columns=['time', 'open', 'high', 'low', 'close',
                                 'volume', 'pct%'])
    return data


def load_daily_qkl123(name1, root_dir=None):
    fdir = find_target_dir('{}/qkl123/'.format(name1),
                           root_dir=root_dir)
    fpath = fdir + '{}-币价走势.csv'.format(name1.upper())
    df = load_csv(fpath).rename(columns={'时间': 'time', '币价': 'close'})
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df['date'] = df['time']
    df.sort_values('date', ascending=True, inplace=True)
    df.set_index('date', inplace=True)
    return df


def load_daily_crypto_usdt(name1, name2=None, mkt='binance',
                           root_dir=None, logger=None):
    '''
    读取BTC和ETH对USDT日行情数据
    
    Examples
    --------
    >>> df_eth = load_daily_crypto_usdt('eth', 'eth_usdt')
    >>> df_btc = load_daily_crypto_usdt('btc', 'btc_usdt')
    '''
    if isnull(name2):
        name2 = name1 + '_usdt'
    name1, name2 = name1.lower(), name2.lower()
    assert name1 in ['btc', 'eth'], '`name1`只能是`btc`或`eth`！'
    df0 = load_ccxt_daily(name1, name2, mkt, root_dir)
    df0['data_source'] = 'binance'
    df0['idx'] = range(0, df0.shape[0])
    df1 = load_daily_btc126(name1, root_dir)
    df1['data_source'] = 'btc126'
    df1['idx'] = range(df0.shape[0], df0.shape[0]+df1.shape[0])
    df2 = load_daily_qkl123(name1, root_dir)
    df2['data_source'] = 'qkl123'
    df2['idx'] = range(df0.shape[0]+df1.shape[0], df0.shape[0]+df1.shape[0]+df2.shape[0])
    df = pd.concat((df0, df1, df2), axis=0)
    df.sort_values(['time', 'idx'], inplace=True)
    df.drop_duplicates(subset=['time'], keep='first', inplace=True)
    loss_dates = check_date_loss(df, only_workday=False, del_weekend=False)
    if len(loss_dates) > 0:
        logger_show('{}日线数据有缺失日期：'.format(name1.upper())+','.join(loss_dates),
                    logger, 'warn')
    return df.reindex(columns=['time', 'open', 'high', 'low', 'close', 'volume', 'data_source'])
    

def get_path_ccxt_minute(name1, name2, minute=15,
                         mkt='binance', root_dir=None):
    fdir = find_target_dir('{}/ccxt_{}/'.format(name1, mkt),
                           root_dir=root_dir)
    fpath = fdir + '{}_{}minute.csv'.format(name2, int(minute))
    return fpath


def load_ccxt_minute(name1, name2, minute=15,
                     mkt='binance', root_dir=None,
                     start_time=None, end_time=None):
    '''
    读取ccxt数字货币行情分钟数据
    
    Examples
    --------
    >>> df_eth_15m = load_ccxt_minute('eth', 'eth_usdt')
    >>> df_btc_5m = load_ccxt_minute('btc', 'btc_usdt', 5)
    >>> df_btc_1m = load_ccxt_minute('btc', 'btc_usdt', 1,
    >>>                              start_time='2022-02-01 05:00:00',
    >>>                              end_time='2022-06-09 14:00:00')
    '''
    fpath = get_path_ccxt_minute(name1, name2,
                                 minute=minute,
                                 mkt=mkt, root_dir=root_dir)
    fpaths = find_paths_year(fpath)
    df = load_csvs(fpaths)
    df.sort_values('time', ascending=True, inplace=True)
    if not start_time is None:
        df = df[df['time'] >= start_time]
    if not end_time is None:
        df = df[df['time'] <= end_time]
    # df.set_index('time', inplace=True)
    return df

#%%
def get_path_trade_dates_tushare(exchange='SSE', root_dir=None):
    fdir = find_target_dir('trade_dates/tushare/', root_dir=root_dir)
    fpath = fdir + '{}.csv'.format(exchange)
    return fpath


def load_trade_dates_tushare(exchange='SSE', root_dir=None):
    '''
    读取交易所交易日历历史数据
    
    Examples
    --------
    >>> df_trade_dates = load_trade_dates_tushare()
    '''
    fpath = get_path_trade_dates_tushare(exchange=exchange,
                                         root_dir=root_dir)
    df= load_csv(fpath)
    df.sort_values('date', ascending=True, inplace=True)
    df.drop_duplicates(subset=['date'], keep='last', inplace=True)
    return df

#%%
def get_path_index_info_tushare(market, root_dir=None):
    fdir = find_target_dir('index/tushare/index_info/',
                           root_dir=root_dir)
    fpath = fdir + '{}.csv'.format(market)
    return fpath


def load_index_info_tushare(market, root_dir=None):
    '''
    根据market读取tushare指数基本信息数据
    
    Examples
    --------
    >>> df_sse = load_index_info_tushare('SSE')
    '''
    fpath = get_path_index_info_tushare(market,
                                        root_dir=root_dir)
    return load_csv(fpath, encoding='gbk')


def load_index_info_all_tushare(root_dir=None):
    '''读取tushare全部指数基本信息数据'''
    fdir = find_target_dir('index/tushare/index_info/',
                           root_dir=root_dir)
    mkts = os.listdir(fdir)
    mkts = [x for x in mkts if x.endswith('.csv')]
    df = []
    for mkt in mkts:
        fpath = fdir + mkt
        df.append(load_csv(fpath, encoding='gbk'))
    df = pd.concat(df, axis=0)
    return df


def get_index_code_name_tushare():
    '''获取tushare所有指数代码和对应简称，返回dict'''
    all_indexs = load_index_info_all_tushare().set_index('code')
    code_names = all_indexs['简称'].to_dict()
    return code_names
    

def find_index_code_tushare(info, root_dir=None, logger=None):
    '''传入code查找对应tushare的code'''
    fdir = find_target_dir('index/tushare/',
                           root_dir=root_dir)
    indexs = os.listdir(fdir)
    for x in indexs:
        if info in x:
            return x
    if info in TS_NAME_CODE.keys():
        return TS_NAME_CODE[info]
    code_names = get_index_code_name_tushare()
    for k, v in code_names.items():
        if info in k or info == v:
            return k
    logger_show('未找到`{}`对应指数代码，返回None，请检查输入！'.format(info),
                logger, 'warn')
    return None


def get_path_index_daily_tushare(code, root_dir=None):
    ts_code = find_index_code_tushare(code)
    fdir = find_target_dir('index/tushare/{}/'.format(ts_code),
                           root_dir=root_dir)
    fpath = fdir + '{}_daily.csv'.format(ts_code)
    return fpath
    

def load_index_daily_tushare(code, root_dir=None):
    '''
    读取tushare指数日线数据
    
    Examples
    --------
    >>> df = load_index_daily_tushare('中证1000')
    >>> df_sh = load_index_daily_tushare('000001.SH')
    >>> df_hs300 = load_index_daily_tushare('000300.SH')
    >>> df_hs300_ = load_index_daily_tushare('399300.SZ')
    >>> df_zz500 = load_index_daily_tushare('000905.SH')
    '''
    fpath = get_path_index_daily_tushare(code, root_dir=root_dir)
    df = load_csv(fpath)
    df.sort_values('date', ascending=True, inplace=True)
    df.drop_duplicates(subset=['date'], keep='last', inplace=True)
    return df


def get_path_index_daily_basic_tushare(code, root_dir=None):
    ts_code = find_index_code_tushare(code)
    fdir = find_target_dir('index/tushare/{}/'.format(ts_code),
                           root_dir=root_dir)
    fpath = fdir + '{}_daily_basic.csv'.format(ts_code)
    return fpath


def load_index_daily_basic_tushare(code, root_dir=None):
    '''
    读取tushare指数日线数据
    
    Examples
    --------
    >>> df = load_index_daily_basic_tushare('沪深300')
    >>> df_sh_basic = load_index_daily_basic_tushare('000001.SH')
    >>> df_hs300_basic = load_index_daily_basic_tushare('000300.SH')
    >>> df_zz500_basic = load_index_daily_basic_tushare('000905.SH')
    '''
    fpath = get_path_index_daily_basic_tushare(code, root_dir=root_dir)
    df = load_csv(fpath, encoding='gbk')
    df.sort_values('date', ascending=True, inplace=True)
    df.drop_duplicates(subset=['date'], keep='last', inplace=True)
    return df


def get_path_index_joinquant(code, freq='daily', root_dir=None):
    fdir = find_target_dir('index/joinquant/')
    fpath = '{}{}_{}.csv'.format(fdir, code, freq)
    if not os.path.exists(fpath):
        code = find_index_code_tushare(code, root_dir)
        code = code.replace('.SZ', '.XSHE').replace('.SH', '.XSHG')
        fpath = '{}{}_{}.csv'.format(fdir, code, freq)
    return fpath


def load_index_joinquant(code, freq='daily', root_dir=None):
    '''
    读取聚宽指数行情数据
    
    Examples
    --------
    >>> df = load_index_joinquant('沪深300')
    '''
    fpath = get_path_index_joinquant(code, freq=freq, root_dir=root_dir)
    fpaths = find_paths_year(fpath)
    df = load_csvs(fpaths)
    return df

#%%
def get_path_astocks_list_tushare(root_dir=None):
    fdir = find_target_dir('stocks/tushare/',
                           root_dir=root_dir)
    fpath = fdir+'astocks_list.csv'
    return fpath


def load_astocks_list_tushare(root_dir=None, del_dup=True):
    '''
    导入A股列表数据
    
    Examples
    --------
    >>> df_a = load_astocks_list_tushare()
    '''
    fpath = get_path_astocks_list_tushare(root_dir=root_dir)
    df = load_csv(fpath, encoding='gbk')
    df.sort_values(['code', 'list_date'],
                   ascending=True, inplace=True)
    if del_dup:
        df.drop_duplicates(subset=['code'],
                           keep='last', inplace=True)
    return df


def find_stocks_code_tushare(infos, root_dir=None,
                             logger=None):
    '''查找股票代码，codes为str或list'''
    def _return(cd):
        _cd = {}
        for x in infos:
            if x in cd:
                _cd[x] = cd[x]
            else:
                logger_show('未找到`{}`对应代码'.format(x),
                            logger, 'warn')
                _cd[x] = None
        if _str:
            return list(_cd.values())[0]
        return _cd
    assert isinstance(infos, (str, list, tuple))
    _str = False
    if isinstance(infos, str):
        _str = True
        infos = [infos]
    cd = {}
    for x in infos:
        x_, sure = get_code_ext(x, True)
        if sure:
            cd[x] = x_
    left = [x for x in infos if x not in cd]
    if len(left) == 0:
        return _return(cd)
    df = load_astocks_list_tushare(root_dir=root_dir)
    df['code_'] = df['code'].copy()
    df_ = df[df['code'].isin(infos)].copy()
    cd.update(df_.set_index('code')['code_'].to_dict())
    left = [x for x in infos if x not in cd]
    if len(left) == 0:
        return _return(cd)
    df_ = df[df['symbol'].isin(infos)].copy()
    cd.update(df_.set_index('symbol')['code_'].to_dict())
    left = [x for x in infos if x not in cd]
    if len(left) == 0:
        return _return(cd)
    df_ = df[df['name'].isin(infos)].copy()
    cd.update(df_.set_index('name')['code_'].to_dict())
    return _return(cd)


def get_path_stock_daily_tushare(code, ext='', root_dir=None):
    assert ext in ['', 'stk', 'basic']
    code = find_stocks_code_tushare(code, root_dir)
    fdir = find_target_dir('stocks/tushare/{}/'.format(code))
    if ext == '':
        fpath = '{}/{}_daily.csv'.format(fdir, code)
    elif ext in ['stk', 'basic']:
        fpath = '{}/{}_daily_{}.csv'.format(fdir, code, ext)
    return fpath


def _load_stock_daily_tushare(code, ext='', root_dir=None):
    '''读取tushare股票日线数据'''
    fpath = get_path_stock_daily_tushare(code, ext=ext, root_dir=root_dir)
    return load_csv(fpath)


def load_stock_daily_tushare(code, ext='', root_dir=None):
    '''
    读取tushare股票日线数据
    
    Examples
    --------
    >>> df = load_stock_daily_tushare('同花顺')
    >>> df = load_stock_daily_tushare('600570.SH')
    '''
    assert isinstance(ext, (str, list, tuple))
    if isinstance(ext, str):
        ext = [ext]
    df = _load_stock_daily_tushare(code, ext[0], root_dir)
    if len(ext) == 0:
        df.sort_values(['code', 'date'], inplace=True)
        return df
    for k in range(1, len(ext)):
        df_ = _load_stock_daily_tushare(code, ext[k], root_dir)
        df = merge_df(df, df_, on=['code', 'date'], how='outer')
    df.sort_values(['code', 'date'], inplace=True)
    return df

#%%
def get_path_chn_bond_yields(cate='national', root_dir=None):
    fdir = find_target_dir('chn_bonds/{}/'.format(cate),
                           root_dir=root_dir)
    fpath = fdir+'chn_{}_bond_rates.csv'.format(cate)
    return fpath


def load_chn_bond_yields(cate='national', root_dir=None):
    '''
    读取国债收益率历史数据
    
    Examples
    --------
    >>> df_chn_bonds = load_chn_bond_yields()
    >>> df_chn_bonds_local = load_chn_bond_yields('local')
    '''
    fpath = get_path_chn_bond_yields(cate=cate,
                                     root_dir=root_dir)
    df = load_csv(fpath, encoding='gbk')
    df.rename(columns={'日期': 'date'}, inplace=True)
    df.sort_values('date', ascending=True, inplace=True)
    df.drop_duplicates(subset=['date'], keep='last', inplace=True)
    return df

#%%
def get_path_cffex_lhb_future(code, date, root_dir=None):
    fdir = find_target_dir('futures/cffex/lhb/{}/'.format(code),
                           root_dir=root_dir)
    date = date_reformat(date, '')
    fpath = '{}{}{}.csv'.format(fdir, code, date)
    return fpath


def load_cffex_lhb_future(code, date, root_dir=None):
    '''
    读取中金所期货龙虎榜数据
    
    Examples
    --------
    >>> df_cffex = load_cffex_lhb_future('IF', '2022-06-10')
    '''
    fpath = get_path_cffex_lhb_future(code, date,
                                      root_dir=root_dir)
    df = load_text_multi(fpath, encoding='gbk')
    return df

#%%
def get_path_futures_info_tushare(exchange, root_dir=None):
    fdir = find_target_dir('futures/tushare/futures_info/',
                           root_dir=root_dir)
    fpath = fdir + exchange + '.csv'
    return fpath


def load_futures_info_tushare(exchange=None, root_dir=None):
    '''
    | 读取期货基本信息数据
    | exchange指定交易所，不指定则读取所有的
    
    Examples
    --------
    >>> df = load_futures_info_tushare()
    >>> df = load_futures_info_tushare('CFFEX')
    '''
    pdir = find_target_dir('futures/tushare/futures_info/',
                           root_dir=root_dir)
    if isnull(exchange):
        fpaths = os.listdir(pdir)
        fpaths = [pdir+x for x in fpaths if x[-4:] == '.csv']
    else:
        fpaths = [pdir+exchange+'.csv']
    df = load_csvs(fpaths, encoding='gbk')
    return df


def find_futures_exchange_tushare(infos, root_dir=None,
                                  logger=None):
    '''
    根据期货合约代码或名称查找所在交易所，codes为str或list
    
    Examples
    --------
    >>> find_futures_exchange_tushare('IF2209')
    'CFFEX'
    '''
    def _return(ex):
        _ex = {}
        for k, v in codes_.items():
            if k in ex:
                _ex[k] = ex[k]
            elif v in ex:
                _ex[k] = ex[v]
            else:
                logger_show('未找到`{}`对应交易所'.format(k),
                            logger, 'warn')
                _ex[k] = None
        if _str:
            return list(_ex.values())[0]
        return _ex
    assert isinstance(infos, (str, list, tuple))
    _str = False
    if isinstance(infos, str):
        _str = True
        infos = [infos]
    codes_ = {x: TS_NAME_CODE[x] if x in TS_NAME_CODE else x for x in infos}
    infos = [TS_NAME_CODE[x] if x in TS_NAME_CODE else x for x in infos]
    ex = {}
    ex_ = {'.CFX': 'CFFEX', '.ZCE': 'CZCE', '.INE': 'INE',
           '.DCE': 'DCE', '.SHF': 'SHFE'}
    ex.update({x: ex_['.'+x.split('.')[-1]] for x in infos if '.'+x.split('.')[-1] in ex_.keys()})
    left = [x for x in infos if x not in ex]
    if len(left) == 0:
        return _return(ex)
    df = load_futures_info_tushare(root_dir=root_dir)
    df_ = df[df['code'].isin(infos)].copy()
    ex.update(df_.set_index('code')['交易市场'].to_dict())
    left = [x for x in infos if x not in ex]
    if len(left) == 0:
        return _return(ex)
    df['code'] = df['code'].apply(lambda x: x.split('.')[0])
    df_ = df[df['code'].isin(infos)].copy()
    ex.update(df_.set_index('code')['交易市场'].to_dict())
    left = [x for x in infos if x not in ex]
    if len(left) == 0:
        return _return(ex)
    df_ = df[df['简称'].isin(infos)].copy()
    ex.update(df_.set_index('简称')['交易市场'].to_dict())
    return _return(ex)


def find_futures_code_tushare(infos, root_dir=None,
                              logger=None):
    '''
    查找期货合约代码，codes为str或list
    
    Examples
    --------
    >>> find_futures_code_tushare('IF2209')
    '''
    def _return(cd):
        _cd = {}
        for x in infos:
            if x in cd:
                _cd[x] = cd[x]
            else:
                logger_show('未找到`{}`对应代码'.format(x),
                            logger, 'warn')
                _cd[x] = None
        if _str:
            return list(_cd.values())[0]
        return _cd
    assert isinstance(infos, (str, list, tuple))
    _str = False
    if isinstance(infos, str):
        _str = True
        infos = [infos]
    cd = {x: TS_NAME_CODE[x] for x in infos if x in TS_NAME_CODE}
    left = [x for x in infos if x not in cd]
    if len(left) == 0:
        return _return(cd)
    df = load_futures_info_tushare(root_dir=root_dir)
    df['code_'] = df['code'].copy()
    df_ = df[df['code'].isin(infos)].copy()
    cd.update(df_.set_index('code')['code_'].to_dict())
    left = [x for x in infos if x not in cd]
    if len(left) == 0:
        return _return(cd)
    df['code'] = df['code'].apply(lambda x: x.split('.')[0])
    df_ = df[df['code'].isin(infos)].copy()
    cd.update(df_.set_index('code')['code_'].to_dict())
    left = [x for x in infos if x not in cd]
    if len(left) == 0:
        return _return(cd)
    df_ = df[df['简称'].isin(infos)].copy()
    cd.update(df_.set_index('简称')['code_'].to_dict())
    return _return(cd)


def get_path_future_daily_ex_tushare(exchange, root_dir=None):
    fdir = find_target_dir('futures/tushare/futures_daily/',
                           root_dir=root_dir)
    fpath = fdir + exchange + '.csv'
    return fpath
        
    
def load_future_daily_ex_tushare(exchange, root_dir=None):
    '''
    读取tushare交易所期货日线数据
    
    Examples
    --------
    >>> load_future_daily_ex_tushare('SSE')
    '''
    fpath = get_path_future_daily_ex_tushare(exchange,
                                             root_dir=root_dir)
    fpaths = find_paths_year(fpath)
    df = load_csvs(fpaths, encoding='gbk')
    df.sort_values(['date', 'code'], ascending=True,
                   inplace=True)
    return df


def get_path_future_daily_tushare(ts_code, root_dir=None):
    fdir = find_target_dir('futures/tushare/', root_dir=root_dir)
    fpath = fdir + '{}/{}_daily.csv'.format(ts_code, ts_code)
    return fpath


def load_future_daily_tushare(code, root_dir=None, logger=None):
    '''
    读取tushare期货日线数据，code为tushare代码
    
    Examples
    --------
    >>> df_if = load_future_daily_tushare('IF.CFX')
    >>> df_ic = load_future_daily_tushare('IC')
    '''
    fdir = find_target_dir('futures/tushare/', root_dir=root_dir)
    files = os.listdir(fdir)
    if code in files:
        fpath = fdir + '{}/{}_daily.csv'.format(code, code)
        return load_csv(fpath, encoding='gbk')
    else:
        exchange = find_futures_exchange_tushare(code, root_dir, logger)
        df = load_future_daily_ex_tushare(exchange, root_dir)
        code = find_futures_code_tushare(code, root_dir, logger)
        return df[df['code'] == code]
    
    
def get_path_future_mindgo(code, freq='daily', root_dir=None):
    fdir = find_target_dir('futures/mindgo/')
    fpath = '{}{}_{}.csv'.format(fdir, code, freq)
    return fpath
    
    
def load_future_mindgo(code, freq='daily', root_dir=None):
    '''
    读取mindgo期货行情数据
    
    Examples
    --------
    >>> df = load_future_mindgo('IF9999')
    >>> df = load_future_mindgo('IF9999', '1min')
    '''
    fpath = get_path_future_mindgo(code, freq=freq, root_dir=root_dir)
    df = load_csv(fpath)
    df.insert(0, 'code', code)
    return df
    
#%%
def get_path_options_info_tushare(exchange, root_dir=None):
    fdir = find_target_dir('options/tushare/options_info/',
                           root_dir=root_dir)
    fpath = fdir + exchange + '.csv'
    return fpath


def load_options_info_tushare(exchange, root_dir=None):
    '''
    读取tushare期权基本信息数据
    
    Examples
    --------
    >>> load_options_info_tushare('SSE')
    '''
    fpath = get_path_options_info_tushare(exchange,
                                          root_dir=root_dir)
    return load_csv(fpath, encoding='gbk')


def get_path_options_daily_ex_tushare(exchange, root_dir=None):
    fdir = find_target_dir('options/tushare/options_daily/',
                           root_dir=root_dir)
    fpath = fdir + exchange + '.csv'
    return fpath


def load_options_daily_ex_tushare(exchange, root_dir=None):
    '''
    读取tushare交易所期权日线数据
    
    Examples
    --------
    >>> df_opt_sse = load_options_daily_ex_tushare('SSE')
    '''
    fpath = get_path_options_daily_ex_tushare(exchange,
                                              root_dir=root_dir)
    fpaths = find_paths_year(fpath)
    df = load_csvs(fpaths)
    df.sort_values(['date', 'code'], ascending=True,
                   inplace=True)
    return df


def load_options_daily_tushare(code, root_dir=None):
    '''读取tushare期权日线数据'''
    raise NotImplementedError

#%%
def get_path_fund_daily_tushare(code, fq='qfq', root_dir=None):
    assert fq in ['', 'qfq', 'hfq']
    if fq != '':
        fq = '_'+fq
    fdir = find_target_dir('fund/tushare/{}/'.format(code),
                           root_dir=root_dir)
    fpath = '{}{}_daily{}.csv'.format(fdir, code, fq)
    return fpath


def load_fund_daily_tushare(code, fq='qfq', root_dir=None):
    '''
    读取tushare基金日线数据
    
    Examples
    --------
    >>> load_fund_daily_tushare('510050.SH')
    '''
    fpath = get_path_fund_daily_tushare(code, fq=fq, root_dir=root_dir)
    df = load_csv(fpath)
    return df

#%%
def _load_stock_daily_tdx(fpath):
    '''
    读取通达信日线.day数据
    
    Note
    ----
    通达信.day为未除权数据，且没有前收盘价列
    
    Examples
    --------
    >>> fpath = 'C:/new_tdx/vipdoc/sh/lday/sh600519.day'
    >>> df = _load_stock_daily_tdx(fpath)
    
    references
    ----------
    - https://www.cnblogs.com/yuyanc/p/16867362.html
    - https://blog.csdn.net/juloong/article/details/127536465
    '''
    res = []
    with open(fpath, 'rb') as f:
        buffer = f.read()
        size = len(buffer)
        row_size = 32 # 每32个字节一个数据
        code = os.path.basename(fpath).replace('.day', '')
        for k in range(0, size, row_size):
            row = list(struct.unpack('IIIIIfII', buffer[k:k+row_size]))
            row[1] = row[1] / 100
            row[2] = row[2] / 100
            row[3] = row[3] / 100
            row[4] = row[4] / 100
            row.insert(0, code)
            row.pop() # TODO: 最后一列为保留值，无意义？
            res.append(row)
    cols = ['code', 'date', 'open', 'high', 'low', 'close', 
            'amount', 'volume']
    df = pd.DataFrame(res)
    df.columns = cols
    return df


def load_stocks_daily_tdx(codes: Union[str, List[str]],
                          tdx_dir: str = None):
    '''
    读取通达信股票日线(.day)数据
    
    Parameters
    ----------
    codes : str, list
        股票代码，格式应如sh600519, sz300033
    tdx_dir : str, None
        | 通达信日线数据根目录，精确到vipdoc，如 `C:/new_tdx/vipdoc/` 
        | 默认在C/D/E/F/G盘下面寻找 `new_tdx/vipdoc/` 文件夹
        
    Examples
    --------
    >>> codes = ['sh600519', 'sz300033'][0]
    >>> tdx_dir = None
    >>> df = load_stocks_daily_tdx(codes, tdx_dir=tdx_dir)
    >>> df = df.sort_values(['code', 'date'], ascending=False)
    '''
    if isna(tdx_dir):
        for rt in ['C', 'D', 'E', 'F']:
            fdir = rt + ':/new_tdx/vipdoc/'
            if os.path.exists(fdir):
                tdx_dir = fdir
                break
    if isna(tdx_dir):
        raise ValueError('未找到通达信vipdoc数据文件夹！')
    codes = check_list_arg(codes)
    codes = [x.lower() for x in codes]
    res = []
    for code in codes:
        mkt = code[:2]
        fpath = tdx_dir + mkt + '/lday/' + code + '.day'
        df = _load_stock_daily_tdx(fpath)
        res.append(df)
    res = pd.concat(res, axis=0)
    res = res.reset_index(drop=True)
    return res

#%%
def _load_stock_daily_ths(fpath):
    '''
    读取同花顺日线.day数据
    
    Note
    ----
    | 同花顺.day为未除权数据，且没有前收盘价列
    | 同花顺.day中成交额数据未精确到个位，只精确到百位，读取数据时直接乘100处理
    
    Examples
    --------
    >>> fpath = 'C:/同花顺软件/同花顺/history/shase/day/600519.day'
    >>> df = _load_stock_daily_ths(fpath)
    >>> df = df.sort_values('date', ascending=False)
    
    references
    ----------
    - https://download.csdn.net/download/dreamerswing/9604512
    '''
    code = os.path.basename(fpath).replace('.day', '')
    res = []
    with open(fpath, 'rb') as f:
        buffer = f.read()
        size = len(buffer)        
        fPoint = 6
        dataNum, fPoint, lineLen, lineCount = \
            struct.unpack_from('<I3H', buffer, fPoint)        
        res = []
        while fPoint < size:
            # TODO: 最后四列为保留值，无意义？
            date, open_, high, low, close, amount, volume, _, _, _, _ = \
                struct.unpack_from('<11I', buffer, fPoint)
            date &= 0x0FFFFFFF
            open_ &= 0x0FFFFFFF
            high &= 0x0FFFFFFF
            low &= 0x0FFFFFFF
            close &= 0x0FFFFFFF
            amount &= 0x0FFFFFFF
            volume &= 0x0FFFFFFF
            res.append([code, date, open_, high, low, close, amount, volume])
            fPoint += lineLen
    df = pd.DataFrame(res)
    cols = ['code', 'date', 'open', 'high', 'low', 'close', 
            'amount', 'volume']
    df.columns = cols
    for c in ['open', 'high', 'low', 'close']:
        df[c] = df[c] / 10000
    df['amount'] = df['amount'] * 100
    return df


def load_stocks_daily_ths(codes: Union[str, List[str]],
                          ths_dir: str = None):
    '''
    读取同花顺股票日线(.day)数据
    
    Parameters
    ----------
    codes : str, list
        股票代码，格式应如600519, 300033
    ths_dir : str, None
        | 同花顺日线数据根目录，精确到history，如 `C:/同花顺软件/同花顺/history/` 
        | 默认在C/D/E/F/G盘下面寻找 `同花顺软件/同花顺/history/` 文件夹
        
    Examples
    --------
    >>> codes = ['600519', '300033']#[0]
    >>> ths_dir = None
    >>> df = load_stocks_daily_ths(codes, ths_dir=ths_dir)
    >>> df = df.sort_values(['code', 'date'], ascending=False)
    '''
    if isna(ths_dir):
        for rt in ['C', 'D', 'E', 'F']:
            fdir = rt + ':/同花顺软件/同花顺/history/'
            if os.path.exists(fdir):
                ths_dir = fdir
                break
    if isna(ths_dir):
        raise ValueError('未找到同花顺vipdoc数据文件夹！')
    codes = check_list_arg(codes)
    codes = [x.lower() for x in codes]
    res = []
    for code in codes:
        mkt = 'shase' if code[0] == '6' else 'sznse'
        fpath = ths_dir + mkt + '/day/' + code + '.day'
        df = _load_stock_daily_ths(fpath)
        res.append(df)
    res = pd.concat(res, axis=0)
    res = res.reset_index(drop=True)
    return res

#%%
if __name__ == '__main__':
    from dramkit import TimeRecoder
    tr = TimeRecoder()
    
    tr.used()







