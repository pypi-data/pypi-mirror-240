# -*- coding: utf-8 -*-

from ._pkg_info import pkg_info
__version__ = pkg_info['__version__']

from .install_check import install_check

from .findata import get_factor_data

from .load_his_data import (load_stock_daily_tushare,
                            load_index_daily_tushare,
                            load_daily_crypto_usdt
                            )
