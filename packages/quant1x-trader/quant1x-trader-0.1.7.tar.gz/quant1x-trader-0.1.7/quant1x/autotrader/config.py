# -*- coding: UTF-8 -*-

from dataclasses import dataclass, field

import yaml

from quant1x.autotrader.base import TradingSession
from quant1x.autotrader.logger import logger
from quant1x.autotrader import env


@dataclass
class TraderConfig:
    # 时间范围 - 持仓卖出
    ask_time: TradingSession = TradingSession("09:51:00~14:59:30")
    # 时间范围 - 撤销订单
    cancel_time: TradingSession = TradingSession("09:15:00~09:19:59, 09:30:00~14:56:59")
    # 时间范围 - 盘中订单
    tick_time: TradingSession = TradingSession("09:30:00-14:57:00")
    # 买入持仓率, 资金控制阀值
    position_ratio: float = 0.5000
    # 买入交易费率
    buy_trade_rate: float = 0.0250
    # TODO: 废弃, 相对开盘价溢价多少买入
    buy_premium_rate: float = 0.0200
    # 印花税, 按照成交金额, 买入没有, 卖出0.1%
    stamp_duty_rate: float = 0.0010
    # 过户费, 按照数量收取, 默认万分之六, 0.06%
    transfer_rate: float = 0.0006
    # 券商佣金, 按成交金额计算, 默认万分之二点五, 0.025%
    commission_rate: float = 0.00025
    # tick订单最大金额
    tick_order_max_amount: float = 10000.00
    # 买入最大金额
    buy_amount_max: float = 250000.00

    def __fix_instance(self):
        """
        加载后修复
        :return:
        """
        if isinstance(self.ask_time, str):
            ts = TradingSession(self.ask_time)
            if ts.is_valid():
                self.ask_time = ts
        if isinstance(self.cancel_time, str):
            ts = TradingSession(self.cancel_time)
            if ts.is_valid():
                self.cancel_time = ts
        if isinstance(self.tick_time, str):
            ts = TradingSession(self.tick_time)
            if ts.is_valid():
                self.tick_time = ts

    def __post_init__(self):
        """
        __init__()后调用, 调整类型
        :return:
        """
        self.__fix_instance()


def load() -> TraderConfig:
    """
    加载配置文件
    :return:
    """
    consts = TraderConfig()
    config_filename = env.get_quant1x_config_filename()
    logger.info(config_filename)
    try:
        with open(config_filename, 'r', encoding='utf-8') as f:
            config_dict = yaml.load(f, Loader=yaml.FullLoader)
            if isinstance(config_dict, dict):
                consts = TraderConfig(**config_dict['trader'])
    except FileNotFoundError:
        logger.error(f"文件未找到：{config_filename}")
    except IsADirectoryError:
        logger.error(f"路径是一个目录：{config_filename}")
    except PermissionError as e:
        logger.error(f"没有权限访问文件：{config_filename}\n错误信息：{e}")
    except Exception as e:
        logger.error(f"发生了一个错误：{config_filename}\n错误信息：{e}")
    # finally:
    #     logger.warning('系统将使用默认配置')
    return consts


if __name__ == '__main__':
    config = load()
    print(config)
