

'''获取项目根目录的绝对路径'''

import os


# 获取根目录的绝对路径
abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼接excel对应的绝对路径
datas_path = os.path.join(abs_path, "datas")
data_path = os.path.join(datas_path, "data.xlsx")

# 拼接config对应的绝对路径
config_path = os.path.join(abs_path, "conf")
case_path = os.path.join(config_path, 'case.conf')
case1_path = os.path.join(config_path, 'case1.conf')
global_path = os.path.join(config_path, 'global.conf')

# 拼接logger.log 文本的路径
logger_path = os.path.join(abs_path, "logs")



