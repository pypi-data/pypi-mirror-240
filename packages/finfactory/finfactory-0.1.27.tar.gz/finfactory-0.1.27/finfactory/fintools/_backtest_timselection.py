# -*- coding: utf-8 -*-

from typing import Dict
from dramkit import (isnull,
                     GenObject)


DEFAULT_PARAMS = {
    'df': None,
    'sig_col': None,
    'sig_type': 1,
    'shift_lag': 0,
    'col_price': 'close',
    'col_price_buy': 'close',
    'col_price_sel': 'close',
    'col_price_high': 'high',
    'col_price_low': 'low',
    'settle_after_act': False,
    'func_vol_add': 'base_1',
    'func_vol_sub': 'base_1',
    'func_vol_stop_loss': 'hold_1',
    'func_vol_stop_gain': 'hold_1',
    'func_vol_add_ext': 'base_1',
    'func_vol_sub_ext': 'base_1',
    'func_stop_loss': None,
    'func_stop_gain': None,
    'func_add_ext': None,
    'func_sub_ext': None,
    'func_fee_buy': 1.5/1000,
    'func_fee_sel': 1.5/100, 
    # 'stop_no_same': True,
    # 'ignore_no_stop': False,
    # 'max_loss': None,
    # 'max_gain': None,
    # 'max_down': None,
    # 'add_loss_pct': None,
    # 'add_gain_pct': None,
    # 'stop_sig_order': 'both',
    # 'add_sig_order': 'offset',
    'hold_buy_max': None,
    'hold_sel_max': None,
    'limit_min_vol': 100,
    'base_vol': None,
    'base_money': 1000000,
    'init_cash': 0.0,
    'sos_money': 1000,
    'force_final0': 'settle',
    'del_begin0': True,
    'gap_repeat': False,
    'nshow': None,
    'logger': None
    }


class TimeSelectionBacktest(object):
    '''择时策略回测'''
    
    def __init__(self, config: dict = None):
        self.cfg = DEFAULT_PARAMS
        if not isnull(config):
            self.cfg.update(config)
        self.cfg = GenObject(dirt_modify=False, **self.cfg)
        
    def _check_cfg(self):
        # if self.cfg.df
        pass
            
        
        