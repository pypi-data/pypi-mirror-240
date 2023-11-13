# -*- coding: UTF-8 -*-
import getpass
import os
import time

import win32com.client
from xtquant.xttrader import XtQuantTrader
from xtquant.xttype import *

from quant1x.qmt.core import *
from quant1x.qmt.logger import logger


def get_gjzq_qmt_exec_path() -> str:
    """
    获取QMT安装路径
    """
    username = getpass.getuser()  # 当前用户名
    qmt_exec_lnk = rf'C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\国金证券QMT交易端\启动国金证券QMT交易端.lnk'
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(qmt_exec_lnk)
    # print(shortcut.Targetpath)
    target_path = str(shortcut.Targetpath)
    paths = target_path.split(r'\bin.x64')
    exec_path = os.path.expanduser(paths[0])
    exec_path = exec_path.replace('\\', '/')
    return exec_path


class Trader(Singleton):
    """
    迅投XtQuant-miniQMT交易
    """
    xt_trader = None
    account = None

    def __del__(self):
        """
        析构方法, 销毁对象
        """
        self.xt_trader.stop()
        logger.info("thinktrader shutdown")

    def set_trader(self, qmt_dir: str = '', session_id: int = 0) -> int:
        qmt_dir.strip()
        if qmt_dir == '':
            qmt_dir = get_gjzq_qmt_exec_path() + '/userdata_mini'
        logger.info("miniQmt: {}", qmt_dir)
        if session_id == 0:
            # session_id为会话编号，策略使用方对于不同的Python策略需要使用不同的会话编号
            now = time.time()
            session_id = int(now)
        logger.info("session id: {}", session_id)
        self.xt_trader = XtQuantTrader(qmt_dir, session_id)
        # 启动交易线程
        self.xt_trader.start()
        # 建立交易连接，返回0表示连接成功
        connect_result = self.xt_trader.connect()
        return connect_result

    def set_account(self, account_id, account_type='STOCK'):
        self.account = StockAccount(account_id, account_type=account_type)
        return self.account

    @property
    def get_account(self):
        return self.account

    @property
    def get_trader(self):
        return self.xt_trader

    def query_asset(self):
        """
        获取资产数据
        :return:
        """
        return self.xt_trader.query_stock_asset(self.get_account)

    def buy(self, code: str, price: float, vol: int, strategy_name='', order_remark='') -> int:
        """
        同步下买单
        """
        order_id = self.xt_trader.order_stock(self.account, code, xtconstant.STOCK_BUY, vol, xtconstant.FIX_PRICE,
                                              price, strategy_name, order_remark)
        return order_id
