# -*- coding: UTF-8 -*-

import os
import time

import pandas as pd

from quant1x.autotrader import market, utils, context, thinktrader, config
from quant1x.autotrader.logger import logger

# 应用名称
application = 'quant1x-trader'


def auto_trader() -> int:
    """
    自动化交易入口
    """
    logger.info('{} start...', application)
    # 0. 加载配置文件
    logger.info('加载配置...')
    conf = config.load()
    logger.info('配置信息: {}', conf)
    logger.info('加载配置...OK')
    trader = thinktrader.ThinkTrader(conf)
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
    # 3.3 检测新增标的
    logger.info('订单路径: {}', ctx.order_path)
    last_mtime = 0
    date_updated = False
    while True:
        time.sleep(1)
        logger.info("检测[交易日]...")
        # 3.3.1 检测当前日期是否最后一个交易日
        (today, trade_date) = trader.current_date()
        if today != trade_date:
            logger.error('today={}, trade_date={}, 非交易日', today, trade_date)
            continue
        elif not date_updated:
            # 如果状态还没调整
            logger.error('today={}, trade_date={}, 当前日期为交易日, 等待开市', today, trade_date)
            ctx.switch_date()
            date_updated = True
        logger.info("检测[交易时段]...")
        if not trader.tick_order_can_trade():
            logger.info('非盘中交易时段, waiting...')
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
            # print(stock)
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

            # 评估可以委托买入的价格和数量
            # 查询计算单一标的可用资金
            single_funds_available = trader.available_amount(stock_total)
            if single_funds_available <= 0:
                logger.warning('!!!已满仓!!!')
                continue
            # 获取快照
            snapshot = trader.get_snapshot(security_code)
            # 计算溢价
            last_price = snapshot['lastPrice']
            buy_price = trader.available_price(last_price)
            # 计算可买数量
            buy_num = trader.calculate_stock_volumes(single_funds_available, buy_price)
            if buy_num < 100:
                logger.warning('单一股价过高, 分仓购买力不足1手')
                stock_total = stock_total - 1
                continue
            logger.warning('{}: 证券名称={}, 证券代码={}, date={}, strategy_code={}, price={},vol={}', strategy_code,
                           security_name, security_code, date, strategy_code, buy_price, buy_num)
            # 委托买入
            order_id = trader.buy(security_code, buy_price, buy_num, strategy_name, 'swfz')
            logger.warning('order id: {}', order_id)
            # 设置执行下单完成状态
            ctx.push_buy_order_done_status(code)

    # 4. 关闭
    logger.info('{} stop...', application)
    trader.stop()
    logger.info('{} stop...OK', application)
    logger.info('{} shutdown', application)
    return 0
