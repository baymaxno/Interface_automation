from configparser import ConfigParser
from common import contants
import os


class Config:
    """读取配置文件类"""

    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read(filenames=contants.global_path, encoding='utf-8')  # 获取开关里的数据
        switch_open = self.conf.getboolean('switch', 'open')
        if switch_open:
            self.conf.read(filenames=contants.case_path, encoding='utf-8')  # 获取环境1里的数据
        else:
            self.conf.read(filenames=contants.case1_path, encoding='utf-8')  # 获取环境2里的数据

    def get_values(self, section, option):
        value = self.conf.get(section=section, option=option)
        try:  # try用来判断是否是字符串  不需要修改类型   利用eval函数  报错的话就是原本类型就是字符串
            if value == 'all':
                return value
            else:
                return eval(value)
        except Exception as e:
            return value


if __name__ == '__main__':
    conf = Config()
    value = conf.get_values('api', 'per_url')
    print(value)