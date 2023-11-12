# coding=utf-8
import os
import platform
import time

import pandas as pd
import yaml
from xtquant.xttype import StockAccount

from quant1x.autotrader import utils, env
from quant1x.autotrader.logger import logger


class QmtContext(object):
    """
    QMT 上下文
    """
    current_date: str  # 当前日期
    config_filename: str  # 配置文件名
    order_path: str  # 运行路径
    account_id: str  # 账号ID
    t89k_order_file: str  # 订单文件
    t89k_flag_ready: str  # 订单就绪标志
    t89k_flag_done: str  # 订单执行完成标志

    def __init__(self):
        self.current_date = time.strftime(utils.kFormatFileDate)
        self.config_filename = env.get_quant1x_config_filename()
        logger.info('配置文件:{}', self.config_filename)
        if not os.path.isfile(self.config_filename):
            print('QMT config %s: 不存在' % self.config_filename)
            exit(utils.errno_config_not_exist)
        with open(self.config_filename, 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
            self.account_id = str(result['order']['account_id'])
            self.order_path = str(result['order']['order_path'])
            self.switch_date()

    def account(self) -> StockAccount:
        return StockAccount(self.account_id)

    def sell_is_ready(self) -> bool:
        """
        卖出条件是否就绪
        :return:
        """
        timestamp = time.strftime(utils.kTimestamp)
        return utils.ask_begin <= timestamp <= utils.ask_end

    def buy_is_ready(self) -> bool:
        """
        买入订单是否准备就绪
        :return:
        """
        if not os.path.isfile(self.t89k_flag_ready) or not os.path.isfile(self.t89k_order_file):
            return False
        return True

    def load_order(self) -> pd.DataFrame:
        """
        加载订单
        :return:
        """
        df = pd.read_csv(self.t89k_order_file)
        return df

    def switch_date(self):
        """
        重置属性
        :return:
        """
        logger.warning("switch_date...")
        self.current_date = time.strftime(utils.kFormatFileDate)
        logger.warning("switch_date...{}", self.current_date)
        flag = 'head'
        self.t89k_flag_ready = os.path.join(self.order_path, f'{self.current_date}-{flag}.ready')
        self.t89k_flag_done = os.path.join(self.order_path, f'{self.current_date}-{flag}-{self.account_id}.done')
        self.t89k_order_file = os.path.join(self.order_path, f'{self.current_date}-{flag}.csv')

    def order_buy_completed(self):
        """
        买入操作完成
        :return:
        """
        self._push_local_message(self.t89k_flag_done)
        print('订单买入操作完成')

    def check_buy_order_done_status(self, code: str) -> bool:
        """
        检查买入订单执行完成状态
        :return:
        """
        flag = self.get_order_flag(code, 1)
        return os.path.exists(flag)

    def push_buy_order_done_status(self, code: str):
        """
        推送买入订单完成状态
        :param ctx:
        :param code:
        :return:
        """
        flag = self.get_order_flag(code, 1)
        self._push_local_message(flag)

    def _push_local_message(self, filename: str):
        """
        推送消息
        :param filename:
        :return:
        """
        with open(filename, 'w') as done_file:
            pass

    def get_order_flag(self, code: str, type: int) -> str:
        """
        获取订单标识
        :param self:
        :param code:
        :param type: 1-b,2-s
        :return:
        """
        today = time.strftime(utils.kFormatFileDate)
        order_type = "b" if type == 1 else "s"
        stock_order_flag = os.path.join(self.order_path, f'{today}-{self.account_id}-{code}-{order_type}.done')
        return stock_order_flag

    def fix_security_code(self, symbol: str) -> str:
        """
        调整证券代码
        :param symbol:
        :return:
        """
        security_code = ''
        if len(symbol) == 6:
            flag = self.get_security_type(symbol)
            security_code = f'{symbol}.{flag}'
        elif len(symbol) == 8 and symbol[:2] in ["sh", "sz", "SH", "SZ"]:
            security_code = symbol[2:] + '.' + symbol[:2].upper()
        else:
            raise utils.errBadSymbol
        return security_code

    def get_security_type(self, symbol: str) -> str:
        """
        获取股票市场标识
        :param symbol:  代码
        :return:
        """
        if len(symbol) != 6:
            raise utils.errBadSymbol
        code_head = symbol[:2]
        if code_head in ["00", "30"]:
            return "SZ"
        if code_head in ["60", "68"]:  # 688XXX科创板
            return "SH"
        if code_head in ["510"]:
            return "SH"
        raise utils.errBadSymbol
