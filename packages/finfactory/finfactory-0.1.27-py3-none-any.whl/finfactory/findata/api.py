# -*- coding: utf-8 -*-

import requests


# 服务信息
SERV_URL = 'http://127.0.0.1:8000'
# SERV_URL = 'http://192.168.0.107:8001'
SERV_URL = 'https://3932w73a92.51vip.biz'


# TODO: 表中无数据时报错处理


def get_factor_data(factors=None, codes=None,
                    start_time=None, end_time=None):
    url = '{}/get_factor_data'.format(SERV_URL)
    params = {
        'factors': factors,
		'codes': codes,
		'start_time': start_time,
		'end_time': end_time,
	}
    res = requests.request('GET', url,
                           params=params)
    return res.json()


def get_data(factors=None, codes=None,
                    start_time=None, end_time=None):
    url = '{}/get_data'.format(SERV_URL)
    params = {
        'factors': factors,
		'codes': codes,
		'start_time': start_time,
		'end_time': end_time,
	}
    res = requests.request('POST', url,
                           params=params)
    return res.json()


if __name__ == '__main__':
    
    # res = get_factor_data(factors='factor_1',
    #                       codes='000001.SH,000300.SH',
    #                       start_time='2022-09-01',
    #                       end_time='2022-09-15',
    #                       )
    res = get_data(factors='factor_1',
                    codes='000001.SH,000300.SH',
                    start_time='2022-09-01',
                    end_time='2022-09-15',
                    )
    # res = get_factor_data(factors='',
    #                       codes='',
    #                       start_time='2001-09-01',
    #                       end_time='2022-09-16')
    print(res)
