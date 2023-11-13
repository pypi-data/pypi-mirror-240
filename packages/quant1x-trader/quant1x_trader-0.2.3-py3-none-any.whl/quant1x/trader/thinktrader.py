# -*- coding: UTF-8 -*-
import math
from typing import Tuple, Any

from xtquant import xtdata
from xtquant.xttrader import XtQuantTrader
from xtquant.xttype import *

from quant1x.trader import env, utils
from quant1x.trader.base import *
from quant1x.trader.config import TraderConfig
from quant1x.trader.logger import logger


class ThinkTrader(Singleton):
    """
    迅投XtQuant-miniQMT交易
    """
    xt_trader = None
    account = None

    def __init__(self, conf: TraderConfig):
        """
        初始化
        :param conf:
        """
        super().__init__()
        # self._ctx = None
        self._config = conf

    def stop(self):
        """
        析构方法, 销毁对象
        """
        if self.xt_trader is not None:
            self.xt_trader.stop()
        logger.info("thinktrader shutdown")

    def set_trader(self, qmt_dir: str = '', session_id: int = 0) -> int:
        qmt_dir.strip()
        if qmt_dir == '':
            qmt_dir = env.get_gjzq_qmt_exec_path() + '/userdata_mini'
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

    def query_asset(self) -> XtAsset:
        """
        获取资产数据
        :return:
        """
        return self.xt_trader.query_stock_asset(self.get_account)

    def account_available(self) -> tuple[float, float]:
        """
        可用资金
        :return:
        """
        asset = self.query_asset()
        if asset is None:
            return 0.00, 0.00
        return asset.total_asset, asset.cash

    def asset_can_trade(self) -> bool:
        """
        资产是否可交易
        :return:
        """
        _, available = self.account_available()
        return available > self._config.keep_cash

    def single_available(self, total: int) -> float:
        """
        调整单一可用资金
        :param asset:
        :param total:
        :return:
        """
        # 查询 总资产和可用
        quant_balance, quant_available = self.account_available()
        if quant_available / quant_balance > self._config.position_ratio:
            quant_available = quant_balance * self._config.position_ratio
        if total > 0:
            single_funds_available = quant_available / total
        else:
            single_funds_available = 0.00
        # 检查最大值
        if single_funds_available > self._config.buy_amount_max:
            single_funds_available = self._config.buy_amount_max
        return single_funds_available

    def available_amount(self, stock_total: int) -> float:
        """
        计算单一标的可用金额
        :param stock_total: 股票总数
        :return:
        """
        single_funds_available = self.single_available(stock_total)
        if single_funds_available <= 100:
            return 0.00
        return single_funds_available

    def available_amount_for_tick(self, stock_total: int) -> float:
        """
        计算单一标的可用金额
        :param stock_total: 股票总数
        :return:
        """
        single_funds_available = self.available_amount(stock_total)
        if single_funds_available <= 100:
            return 0.00
        if single_funds_available > self._config.tick_order_max_amount:
            # 超出81号策略单只个股最大买入金额
            single_funds_available = self._config.tick_order_max_amount
        return single_funds_available

    def get_snapshot(self, security_code: str = '') -> Any:
        """
        获得快照
        :param security_code:
        :return:
        """
        tick_list = xtdata.get_full_tick([security_code])
        if len(tick_list) != 1:
            return None
        snapshot = tick_list[security_code]
        return snapshot

    def available_price(self, price: float) -> float:
        """
        计算适合的买入价格
        :param price:
        :return:
        """
        lastPrice = price
        # 价格笼子, +2%和+0.10哪个大
        buy_price = max(lastPrice * 1.02, lastPrice + 0.10)
        # 当前价格+0.05
        # buy_price = snapshot['askPrice'][0] + 0.05
        buy_price = lastPrice + 0.05
        # 最后修订价格
        buy_price = utils.price_round(buy_price)
        return buy_price

    def calculate_buy_fee(self, price: float, volume: int) -> float:
        """
        计算买入的总费用
        :return: 股票数量
        """
        # 1. 印花税, 按照成交金额计算, 买入没有, 卖出, 0.1%
        _stamp_duty_fee = utils.price_round(volume * price * self._config.stamp_duty_rate_for_buy)
        # 2. 过户费, 按照股票数量, 双向, 0.06%
        _transfer_fee = utils.price_round(volume * self._config.transfer_rate)
        # 3. 券商佣金, 按照成交金额计算, 双向, 0.025%
        _commission_fee = utils.price_round(volume * price * self._config.commission_rate)
        if _commission_fee < self._config.commission_min:
            _commission_fee = self._config.commission_min
        # 4. 股票市值
        _stock_fee = utils.price_round(volume * price)
        _fee = (_stamp_duty_fee + _transfer_fee + _commission_fee + _stock_fee)
        logger.debug('综合费用:{}, 委托价格={}, 数量={}, 其中印花说={}, 过户费={}, 佣金={}, 股票={}', _fee, price, volume, _stamp_duty_fee, _transfer_fee, _commission_fee, _stock_fee)
        return _fee

    def calculate_stock_volumes(self, fund: float, price: float) -> int:
        """
        可以购买的股票数量(股)
        :return: 股票数量
        """
        # 1. 印花税, 按照成交金额计算, 买入没有, 卖出, 0.1%
        # stamp_duty = volume * price * stamp_duty_rate
        _stamp_duty_fee = price * self._config.stamp_duty_rate_for_buy
        # 2. 过户费, 按照股票数量, 双向, 0.06%
        # transfer_fee = volume * transfer_rate
        _transfer_fee = self._config.transfer_rate
        # 3. 券商佣金, 按照成交金额计算, 双向, 0.025%
        # commissions = volume * price * commission_rate
        _commission_fee = price * self._config.commission_rate
        # 4. 股票市值
        # _stock_fee= volume * price
        _stock_fee = price
        _fee = (_stamp_duty_fee + _transfer_fee + _commission_fee + _stock_fee)
        volume = fund / _fee
        volume = math.floor(volume / 100) * 100
        # 5. 检查买入总费用, 如果大于预计金额, 则减去100股
        _fee = self.calculate_buy_fee(price, volume)
        if _fee > fund:
            volume = volume - 100
        return volume

    def head_order_can_trade(self) -> bool:
        """
        早盘订单是否可交易
        :return:
        """
        return self._config.head_time.is_trading()

    def tick_order_can_trade(self) -> bool:
        """
        检查盘中订单是否可以交易
        :return:
        """
        return self._config.tick_time.is_trading()

    def tick_order_is_ready(self) -> bool:
        """
        盘中订单是否就绪
        :return:
        """
        return True

    def current_date(self) -> tuple[str, str]:
        """
        今天
        :return:
        """
        today = time.strftime(utils.kFormatOnlyDate)
        v = xtdata.get_market_last_trade_date('SH')
        local_time = time.localtime(v / 1000)
        trade_date = time.strftime(utils.kFormatOnlyDate, local_time)
        return today, trade_date

    def today_is_trading_date(self) -> bool:
        """
        今天是否交易日
        :return:
        """
        (today, trade_date) = self.current_date()
        logger.info('today={}, trade_date={}', today, trade_date)
        return today == trade_date

    def order_can_cancel(self) -> bool:
        """
        委托订单可以撤销
        :return:
        """
        return self._config.cancel_time.is_trading()

    def buy(self, code: str, price: float, vol: int, strategy_name='', order_remark='') -> int:
        """
        同步下买单
        """
        order_id = self.xt_trader.order_stock(self.account, code, xtconstant.STOCK_BUY, vol, xtconstant.FIX_PRICE,
                                              price, strategy_name, order_remark)
        return order_id

    def sell(self, position: XtPosition, strategy_name='', order_remark='') -> int:
        """
        同步下卖单
        """
        order_id = self.xt_trader.order_stock(self.account, position.stock_code, xtconstant.STOCK_SELL,
                                              position.can_use_volume,
                                              xtconstant.LATEST_PRICE,
                                              -1, strategy_name, order_remark)

        return order_id

    def query_positions(self):
        """
        查询持仓  -> list[XtPosition]
        :return:
        """
        positions = self.xt_trader.query_stock_positions(self.account)
        return positions
