import ast
import random
from django.core.cache import cache
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from config.config import Config

Ali = {
    'accesskey_id': Config.getIns().get("xj_short_message", "ALI_ACCESSKEY_ID"),
    'accesskey_secret': Config.getIns().get("xj_short_message", "ALI_ACCESSKEY_SECRET"),
    'sign_name': Config.getIns().get("xj_short_message", "ALI_SIGN_NAME"),
    'template_code': Config.getIns().get("xj_short_message", "ALI_TEMPLATE_CODE"),
}
Tencent = {
    'accesskey_id': Config.getIns().get("xj_short_message", "TENCENT_ACCESSKEY_ID"),
    'accesskey_secret': Config.getIns().get("xj_short_message", "TENCENT_ACCESSKEY_SECRET"),
    'sign_name': Config.getIns().get("xj_short_message", "TENCENT_SIGN_NAME"),
    'template_code': Config.getIns().get("xj_short_message", "TENCENT_TEMPLATE_CODE"),
}


class SendShortMessageService:

    @staticmethod
    def send_sms(phone, platform):
        code = SendShortMessageService.get_code(6, False)  # 生成6位验证码
        cache.set(phone, code, 300)  # 5分钟有效期
        if platform == 'ALi':
            result = SendShortMessageService.ali_send_sms(Ali, code, phone)
            dictionary = ast.literal_eval(result)
            if dictionary['Code'] == 'OK':
                return dictionary, None
            else:
                return None, dictionary['Message']

        elif platform == 'Tencent':
            result = SendShortMessageService.tencent_send_sms(Tencent, code, phone)
            if result['errmsg'] == 'OK':
                return result, None
            else:
                return None, result['errmsg']
        else:
            return None, None

    @staticmethod
    def ali_send_sms(config, code, phone):
        client = AcsClient(config['accesskey_id'], config['accesskey_secret'])
        code = "{'code':%s}" % (code)
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')  # url
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')
        request.add_query_param('RegionId', 'cn-hangzhou')
        request.add_query_param('PhoneNumbers', phone)  # 待发送手机号
        request.add_query_param('SignName', config['sign_name'])  # 短信签名
        request.add_query_param('TemplateCode', config['template_code'])  # 短信模板code
        request.add_query_param('TemplateParam', code)
        response = client.do_action_with_exception(request)
        # python2: print(response)
        return str(response, encoding='utf-8')

    @staticmethod
    def tencent_send_sms(config, code, phone):
        """
          单条发送短信
          :param phone_num: 手机号
          :param template_id: 腾讯云短信模板ID
          :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
          :return:
          """
        appid = config['accesskey_id']  # 自己应用ID
        appkey = config['accesskey_secret']  # 自己应用Key
        sms_sign = config['sign_name']  # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
        template_id = config['template_code']
        template_param_list = [code]
        sender = SmsSingleSender(appid, appkey)
        try:
            response = sender.send_with_param(86, phone, template_id, template_param_list, sign=sms_sign)
        except HTTPError as e:
            response = {'result': 1000, 'errmsg': "网络异常发送失败"}
        return response

    # 数字表示生成几位, True表示生成带有字母的 False不带字母的
    @staticmethod
    def get_code(n=6, alpha=False):
        s = ''  # 创建字符串变量,存储生成的验证码
        for i in range(n):  # 通过for循环控制验证码位数
            num = random.randint(0, 9)  # 生成随机数字0-9
            if alpha:  # 需要字母验证码,不用传参,如果不需要字母的,关键字alpha=False
                upper_alpha = chr(random.randint(65, 90))
                lower_alpha = chr(random.randint(97, 122))
                num = random.choice([num, upper_alpha, lower_alpha])
            s = s + str(num)
        return s
