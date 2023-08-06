#  =============================================================================
#  GNU Lesser General Public License (LGPL)
#
#  Copyright (c) 2022 Qujamlee from www.aztquant.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  =============================================================================

import datetime

from AztVe.common.qujam_struct_for_azt import AztStructs
from .trade_api_struct import PlaceOrder
from ..protos import Trade_Message_pb2 as proto


# 用户注册回复信息
@AztStructs(proto.UserRegisterInfo)
class UserRegisterInfo:
    strategy_id: str = None
    account: str = None
    passwd: str = None
    acc_status: int = None


# 注册回复信息
@AztStructs(proto.RegisterAck)
class RegisterAck:
    registe_info: UserRegisterInfo = None
    regist_code: int = None


# 登录信息
@AztStructs(proto.LoginInfo, adj_time=dict(exchange_time=["%Y%m%d%H%M%S", "%Y%m%d-%H:%M:%S.%f"]))
class LoginInfo:
    account: str = None
    trading_day: str = None
    exchange_name: str = None
    exchange_time: datetime.datetime = None


@AztStructs(proto.LoginAck)
class LoginAck:
    login_info: LoginInfo = None
    ret_code: int = None


# 账户资产信息
@AztStructs(proto.AccMargin,
            amount_dec="amount_decimal_place",
            adj_amount=["total_amount", "available_amount", "deposit", "open_balance", "trade_frozen_margin",
                        "position_market_amount", "total_buy_amount", "total_buy_fee", "total_sell_amount",
                        "total_sell_fee"],
            adj_time=dict(update_time="%Y%m%d"),
            )
class AccMargin:
    account: str = None
    total_amount: float = None
    available_amount: float = None
    deposit: float = None
    open_balance: float = None
    trade_frozen_margin: float = None
    position_market_amount: float = None
    total_buy_amount: float = None
    total_buy_fee: float = None
    total_sell_amount: float = None
    total_sell_fee: float = None
    update_time: datetime.datetime = None


# 入金历史信息
@AztStructs(proto.HisDeposit,
            price_dec="amount_decimal_place",
            adj_price=["deposit"],
            adj_time=dict(settlement_date="%Y%m%d", deposit_time="%Y%m%d-%H:%M:%S.%f"),
            )
class HisDeposit:
    settlement_date: datetime.datetime = None
    account: str = None
    client_ref: str = None
    deposit: float = None
    # deposit_time: datetime.datetime = None


# 历史资金查询回报
@AztStructs(proto.QryHisAccAck, adj_repeat=["acc_margins"])
class QryHisAccAck:
    acc_margins: [AccMargin] = None


# 历史入金查询回报
@AztStructs(proto.QryHisDepositAck, adj_repeat=["his_deposits"])
class QryHisDepositAck:
    his_deposits: [HisDeposit] = None


# 账户入金信息
@AztStructs(proto.AccDepositAck)
class AccDepositAck:
    acc_margin: AccMargin = None
    error_code: int = None


# 委托订单执行状态
@AztStructs(proto.OrdStatusMsg, price_dec="price_decimal_place",
            adj_price=["traded_amount", "total_fee", "frozen_margin", "frozen_price"],
            adj_time=dict(report_time=["%Y%m%d-%H:%M:%S.%f", "%Y%m%d-%H%M%S.%f"]),
            )
class OrdStatusMsg:
    order_status: int = None
    traded_qty: int = None
    traded_amount: float = None
    total_fee: float = None
    frozen_margin: float = None
    frozen_price: float = None
    reject_reason: int = None
    # reject_reason_detail: bytes = None
    report_time: datetime.datetime = None


# 委托订单信息
@AztStructs(proto.OrdReport)
class OrdReport:
    place_order: PlaceOrder = None
    status_msg: OrdStatusMsg = None


# 委托查询回复信息
@AztStructs(proto.QueryOrdersAck, adj_repeat=["order_reports"])
class QueryOrdersAck:
    order_reports: [OrdReport] = None


# 成交回报信息
@AztStructs(proto.TradeReport, price_dec="price_decimal_place", adj_price=["traded_price", "fee"],
            adj_time=dict(transact_time=["%Y%m%d-%H:%M:%S.%f", "%Y%m%d-%H:%M:%S"]))
class TradeReport:
    order_id: str = None
    client_ref: str = None
    account: str = None
    market: str = None
    code: str = None
    traded_id: str = None
    traded_index: int = None
    exec_type: int = None
    traded_qty: int = None
    traded_price: float = None
    fee: float = None
    transact_time: datetime.datetime = None


# 交易明细查询回复信息
@AztStructs(proto.QueryTradesAck, adj_repeat=["trade_reports"])
class QueryTradesAck:
    trade_reports: [TradeReport] = None


# 持仓信息
@AztStructs(proto.StokPosition, price_dec="price_decimal_place", adj_price=["open_avg_price"])
class StockPosition:
    account: str = None
    market: str = None
    code: str = None
    total_qty: int = None
    today_qty: int = None
    open_avg_price: float = None
    surplus_close_qty: int = None
    frozen_qty: int = None
    # update_time: datetime.datetime = None


# 持仓查询回复信息
@AztStructs(proto.QueryPositionsAck, adj_repeat=["positions"])
class QueryPositionsAck:
    positions: [StockPosition] = None


# 撤单拒绝回报
@AztStructs(proto.CancelOrderReject, adj_time=dict(report_time="%Y%m%d-%H:%M:%S.%f"))
class CancelOrderReject:
    client_ref: str = None
    org_order_id: str = None
    reject_reason: int = None
    report_time: datetime.datetime = None
