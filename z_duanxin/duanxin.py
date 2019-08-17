from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError


appid = 14062  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
appkey = "e67d6231bcecc"
# 需要发送短信的手机号码
template_id = 374942  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = '乐途旅游'   # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请

phone_numbers = ["18191337921"]

sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
params = ["希尔顿酒店豪华套房", '999', '2019-08-08']

ssender = SmsSingleSender(appid, appkey)
try:
    result = ssender.send_with_param(86, phone_numbers[0],
                                     template_id, params, sign=sms_sign, extend="", ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
