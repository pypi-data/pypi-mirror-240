import json
from typing import Dict, Optional
from lxmpay.cache import MemoryCache
from lxmpay.core import AsyncPayCore
from lxmpay.errors import PayError
from lxmpay.models import CancelResult, Env, LklPayConfig, PayMethod, PayResult, PayType
from lxmpay import http
from hashlib import md5
import asyncio
lock = asyncio.Lock()

class LakalaPay(AsyncPayCore):
    def __init__(self, config: LklPayConfig):
        self.config = config
        self.end_point = 'http://wyjsdev1.smartac.co/pay' if self.config.env == Env.SANDBOX else 'http://wyjs.smartac.co/pay'
        self.cache = MemoryCache()

    async def login(self):
        url = f'{self.end_point}/v1/auth/token'
        data = {
            'username': self.config.username,
            'password': md5(self.config.password.encode()).hexdigest()
        }
        resp = (await http.post(url, json=data, timeout=self.config.timeout))
        if resp.status_code != 200:
            raise PayError('登录失败 http status code: %s' % resp.status_code)
        resp = resp.json()
        if resp['code'] != 0:
            raise Exception(resp['msg'])
        return 'Bearer '+ resp['data']['token']

    async def save_token(self, token):
        await self.cache.save('token', token, 20 * 60 * 60)

    async def get_token(self):
        async with lock:
            token = await self.cache.get('token')
            if not token:
                token = await self.login()
                await self.cache.save('token', token, 20 * 60 * 60)  #默认24小时有效
            return token

    def get_pay_way(self, pay_type:PayType):
        if pay_type == PayType.Wechat:
            return '2'
        elif pay_type == PayType.Alipay:
            return '1'
        raise Exception('未知的pay_type')
    
    def get_sub_payway(self, pay_method:PayMethod):
        if pay_method == PayMethod.MINIPROG:
            return '4'
        raise Exception('未知的pay_method')

    async def common_header(self):
        return {
            'Authorization': await self.get_token(),
        }

    async def pay(self, out_trade_no: str,
                  total_amount: int,
                  open_id: str,
                  description: str,
                  pay_type: PayType,
                  pay_method: PayMethod,
                  notify_url: Optional[str] = None,
                  reqip: Optional[str] = None,
                  attach: Optional[str] = None, **kwargs) -> PayResult:
        url = f'{self.end_point}/v1/pay/precreate'
        data = {
            'channel_id': self.config.channel_id,
            'client_sn': out_trade_no,
            'total_amount': total_amount,
            'payway': self.get_pay_way(pay_type),
            'sub_payway': self.get_sub_payway(pay_method),
            'open_id': open_id,
            'subject': description,
            'notify_url': notify_url,
            'client_ip': reqip,
        }
        headers = await self.common_header()
        resp = (await http.post(url, headers=headers, json=data, timeout=self.config.timeout))
        if resp.status_code != 200:
            raise PayError('支付失败 http status code: %s' % resp.status_code)
        resp_data = resp.json()
        if resp_data['code'] != 0:
            raise PayError(resp_data['msg'])
        if resp_data['data']['status'] != 'SUCCESS':
            raise PayError(resp_data['data']['error_message'])
        return PayResult(
            code = 0,
            msg = 'success',
            trade_no = resp_data['data']['out_order_id'],
            prepay_data= json.loads(resp_data['data']['wap_pay_request']),
        )
    
    async def cancel(self, refund_trace_no: str, refund_fee: int, out_trade_no: str, trade_no: str = None, **kwargs) -> CancelResult:
        url = f'{self.end_point}/v1/pay/refund'
        data = {
            'channel_idrefund_request_no': refund_trace_no,
            'client_sn': out_trade_no,
            'refund_amount': str(refund_fee),
        }
        headers = await self.common_header()
        resp = (await http.post(url, headers=headers, json=data, timeout=self.config.timeout))
        if resp.status_code != 200:
            raise PayError('退款失败 http status code: %s' % resp.status_code)
        resp_data = resp.json()
        if resp_data['code'] != 0:
            raise PayError(resp_data['msg'])
        if resp_data['data']['status'] != 'SUCCESS':
            raise PayError(resp_data['data']['error_message'])
        return CancelResult(
            code =0,
            msg= 'success',
            refund_fee = resp_data['data']['refund_amount'],
            out_trade_no= resp_data['data']['client_sn'],
            trade_no= resp_data['data']['out_order_id'],
        )

    
if __name__ == '__main__':
    import asyncio
    async def main():
        core = LakalaPay(LklPayConfig(
            env=Env.SANDBOX,
            channel_id='85',
            username='api_pay_open_public_test',
            password='api_pay_open_public_test@2023',
        ))
        import time
        out_trade_no = str(time.time())
        ret = await core.pay(out_trade_no,100,'oRuBz6zFsIEQ750IqcllZPXXozDU','test',PayType.Wechat,PayMethod.MINIPROG)
        print(ret)

        ret = await core.cancel(str(time.time()),1,out_trade_no)
        print(ret)
    asyncio.run(main())