
from typing import Dict, Optional, TypeVar
from lxmpay.core import AsyncPayCore
from lxmpay.lkl_pay import LakalaPay

from lxmpay.models import  LklPayConfig, PayConfig, PayCoreType, PayMethod, PayResult, PayType

CongigType = TypeVar('CongigType', bound=PayConfig)

class AsyncPayClient(AsyncPayCore):

    def __init__(self, config: CongigType):
        self.config = config
        self.pay_core = self.create_core(config)

    def create_core(self, config: CongigType) -> AsyncPayCore:
        if config.pay_core_type == PayCoreType.LKL:
            assert isinstance(config, LklPayConfig)
            return LakalaPay(config)
        raise Exception('未知的支付类型')

    async def pay(self,
                  out_trade_no: str,
                  total_amount: int,
                  open_id: str,
                  description: str,
                  pay_type: PayType,
                  pay_method: PayMethod,
                  notify_url: Optional[str] = None,
                  reqip: Optional[str] = None,
                  attach: Optional[str] = None, **kwargs
                  ) -> PayResult:
        return await self.pay_core.pay(out_trade_no, total_amount, open_id, description, pay_type, pay_method, notify_url=notify_url, reqip=reqip, attach=attach, **kwargs)

    async def cancel(self, refund_trace_no: str, refund_fee: int, out_trade_no: str, trade_no: str = None, **kwargs):
        return await self.cancel(refund_trace_no, refund_fee, out_trade_no, trade_no=trade_no, **kwargs)
