import logging
import os
from common.config import Config
from common import contants

class Logging:
    """日志类"""
    conf = Config()

    def __init__(self, name):
        self.logger = logging.Logger(name=name)  # 新建一个容器
        self.get_level = self.conf.get_values('Log', 'in_level')  # 收集器收集级别
        self.ch_level = self.conf.get_values('Log', 'ch_level')  # 控制台输出级别
        self.fh_level = self.conf.get_values('Log', 'ch_level')  # 文本输出级别
        self.formatter = logging.Formatter(self.conf.get_values('Log', 'formatter'))  # 设置logging输出格式
        self.logger.setLevel(level=self.get_level)  # 设置容器收集级别

    def my_log(self, level, msg, file_name):
        ch = logging.StreamHandler()  # 新建一个控制台输出
        ch.setLevel(self.ch_level)  # 设置控制台输出级别
        ch.setFormatter(self.formatter)  # 设置控制台打印格式

        fh = logging.FileHandler(filename=os.path.join(contants.logger_path, file_name), encoding='utf-8')  # 新建文本输出
        fh.setLevel(self.fh_level)  # 设置文本输出级别
        fh.setFormatter(self.formatter)  # 设置文本输出格式

        # 添加至容器
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        # 判断级别，调用对应的方法
        if level == "DEBUG":
            self.logger.debug(msg)
        elif level == "INFO":
            self.logger.info(msg)
        elif level == "WARNING":
            self.logger.warning(msg)
        elif level == "ERROR":
            self.logger.error(msg)
        else:
            self.logger.critical(msg)

        # 删除容器
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

    def debug(self, msg, file_name):
        self.my_log("DEBUG", msg, file_name)

    def info(self, msg, file_name):
        self.my_log("INFO", msg, file_name)

    def warning(self, msg, file_name):
        self.my_log("WARNING", msg, file_name)

    def error(self, msg, file_name):
        self.my_log("ERROR", msg, file_name)

    def critical(self, msg, file_name):
        self.my_log("CRITICAL", msg, file_name)


if __name__ == '__main__':
    my_logger = Logging('my_logger')
    my_logger.info('这是一条INFO', 'logger.log')