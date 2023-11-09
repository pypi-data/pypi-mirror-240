# -*- coding: UTF-8 -*-
import math
import sys
import os
import time

import pandas as pd

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from xtquant import xtdata

from quant1x.base.logger import logger
from quant1x.trader import market, utils, context
from quant1x.trader import thinktrader

# 应用名称
application = 'quant1x-trader'
# 盘中订单最大金额
TICK_ORDER_MAX_AMOUNT = 10000


def tick_order_is_ready() -> bool:
    """
    盘中订单是否就绪
    :return:
    """
    return True


def mini_qmt_trader() -> int:
    """
    miniQMT代理服务入口
    """
    logger.info('{} start...', application)
    trader = thinktrader.Trader()
    # 1. 连接miniQMT
    connect_result = trader.set_trader()
    if connect_result == 0:
        logger.info('connect miniQmt: success')
    else:
        logger.error('connect miniQmt: failed')
        return utils.errno_miniqmt_connect_failed
    logger.info('{} start...OK', application)
    # 2. 设置账号
    ctx = context.QmtContext()
    trader.set_account(ctx.account_id)
    # 3. 盘中交易流程
    # ret = xtdata.subscribe_whole_quote(['SH', 'SZ'])
    # print(ret)
    # v = xtdata.get_market_last_trade_date('SH')
    # print(v)
    # v = xtdata.get_market_data(stock_list=['600630.sh'], period='tick')
    # code = "sh600630"
    # logger.info(market.fix_security_code(code))
    # v = xtdata.get_full_tick(code_list=['600630.sh'])
    # logger.info(v)
    # 3.3 检测新增标的
    logger.info('订单路径: {}', ctx.order_path)
    last_mtime = 0
    while True:
        time.sleep(1)
        # 3.3.1 检测当前日期是否最后一个交易日
        today = time.strftime(utils.kFormatOnlyDate)
        v = xtdata.get_market_last_trade_date('SH')
        local_time = time.localtime(v / 1000)
        trade_date = time.strftime(utils.kFormatOnlyDate, local_time)
        logger.info('today={}, trade_date={}', today, trade_date)
        if today != trade_date:
            logger.error('today={}, trade_date={}, 非交易日, 退出', today, trade_date)
            continue
        if not utils.current_is_trading():
            logger.info('非交易时段, waiting...')
            continue
        # 3.3.2 检测新标的
        logger.warning('检测新增标的...')
        filename_stock_pool = ctx.order_path + '/stock_pool.csv'
        update_time = os.path.getmtime(filename_stock_pool)
        if update_time == last_mtime:
            logger.warning('检测新增标的...无变化')
            continue
        else:
            last_mtime = update_time
        mtime = time.localtime(last_mtime)
        timestamp = time.strftime(utils.kFormatTimestamp, mtime)
        logger.info('{} last modify: {}', filename_stock_pool, timestamp)
        # 3.3.3 检查当日所有的订单
        df = pd.read_csv(filename_stock_pool)
        if len(df) == 0:
            continue
        # 过滤条件: 当日订单且策略编号为81
        condition = (df['date'] == today) & (df['strategy_code'] == 81)
        tick_orders = df[condition]
        if len(tick_orders) == 0:
            continue
        stock_total = len(tick_orders)
        logger.warning('盘中水位观测: {}', stock_total)
        # 遍历订单
        for idx, stock in tick_orders.iterrows():
            #print(stock)
            date = stock['date']
            code = stock['code']
            # 检查买入状态
            if ctx.check_buy_order_done_status(code):
                # 已经买入跳过
                continue
            strategy_code = stock['strategy_code']
            strategy_name = stock['strategy_name']
            security_name = stock['name']
            security_code = market.fix_security_code(code)
            # 查询证券资产
            asset = trader.query_asset()

            # 计算单一可用资金
            single_funds_available = utils.fix_single_available(asset, stock_total)
            # 扣除可能发生的交易费率
            single_funds_available = single_funds_available * (1 - utils.buy_trade_rete)
            if single_funds_available > TICK_ORDER_MAX_AMOUNT:
                # 超出81号策略单只个股最大买入金额
                single_funds_available = TICK_ORDER_MAX_AMOUNT
            # 获取快照
            tick_list = xtdata.get_full_tick([security_code])
            snapshot = tick_list[security_code]
            # 计算溢价
            # 价格笼子, +2%和+0.10哪个大
            lastPrice = snapshot['lastPrice']
            buy_price = max(lastPrice * 1.02, lastPrice + 0.10)
            # 当前价格+0.05
            buy_price = snapshot['askPrice'][0] + 0.05
            buy_price = utils.price_round(buy_price)
            print(security_code, 'buy:', buy_price)
            buy_num = math.floor(single_funds_available / (buy_price * 100)) * 100
            logger.warning('{}: 证券名称={}, 证券代码={}, date={}, strategy_code={}, price={},vol={}', strategy_code, security_name, security_code, date, strategy_code, buy_price, buy_num)
            order_id  = trader.buy(security_code,buy_price, buy_num, strategy_name, 'swfz')
            logger.warning('order id: {}', order_id)
            # 设置执行下单完成状态
            ctx.push_buy_order_done_status(code)

    # 4. 关闭
    logger.info('{} stop...', application)
    del trader
    logger.info('{} stop...OK', application)
    logger.info('{} shutdown', application)


if __name__ == '__main__':
    sys.exit(mini_qmt_trader())
