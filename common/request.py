import requests
from common.logger import Logging
from common.config import Config
import json


class Request:
    """接口调用，相当于数学类"""

    def __init__(self):
        self.session = requests.sessions.session()  # 实例化一个session    session主要是保存一段时间cookies
        self.logger = Logging('MyLog')

    def request(self, method, url, data=None, headers=None):
        config_url = Config().get_values('api', 'per_url') + url  # 拼接Excel里面与配置文件里的URL  最后取值传入
        method = method.upper()  # 将字符串全部转成大写
        if data is not None and type(data) == str:  # 判断传入的数据是否为空 或者是否为字符串
            data = eval(data)  # 是字符串就转成字典
        if method == 'GET':
            data = json.dumps(data)
            return self.session.request(method, url=config_url, params=data, headers=headers)
        elif method == 'POST':
            data = json.dumps(data)
            return self.session.request(method, url=config_url, data=data, headers=headers)
        else:
            self.logger.error('使用其他的方式！', 'logger.log')


if __name__ == '__main__':
    # import json
    date = {'mobile_phone':15926546345,'pwd':'12345678'}
    # date_json = json.dumps(date)
    url = '/member/login'
    res = Request()
    print(res.request('POST', url, date).text)



    # import json
    # date_1 = {'mobile_phone': 15926546345, 'pwd': '12345678'}
    # d = json.dumps(date_1)
    # res = requests.sessions.session()
    # headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
    # r = res.request(method="POST", url='http://api.lemonban.com/futureloan/member/login', data=d, headers=headers)
    # date_dice = json.loads(r.text)
    # print(r.text)
    # print(date_dice["msg"])