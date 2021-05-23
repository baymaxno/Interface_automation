
import unittest
from common.do_excel import DoExcel
from common.request import Request
from common import contants
from ddt import ddt, data
from common.mysql import MysqlUtil
import json


@ddt()
class TestRegister(unittest.TestCase):
    """注册"""

    do_excel = DoExcel(contants.data_path, 'register')
    cases = do_excel.raed()
    request = Request()
    mysql = MysqlUtil()

    @data(*cases)
    def test_register(self, case):
        db_date = json.loads(case.date)
        if db_date["mobilephone"] == "${mobilephone}":
            sql = "select max(mobilephone) from future.member"
            db_date["mobilephone"] = int(self.mysql.my_sql(sql)[0]) + 1
        print(type(db_date))
        resp = self.request.request(case.method, case.url, db_date)  # 调用接口
        try:
            print('第{0}条用例开始执行！'.format(case.case_id))
            self.assertEqual(str(case.expected), resp.json()['code'])  # 断言
            self.do_excel.write(case.case_id+1, resp.json()['code'], 'PASS')  # 写入结果
            print('第{0}条用例执行结果：{1}'.format(case.case_id,resp.text))
            print('第{0}条用例执行结果：PASS'.format(case.case_id))
        except AssertionError as e:
            self.do_excel.write(case.case_id+1, resp.json()['code'], 'FAIL')
            print('第{0}条用例执行结果：FAIL'.format(case.case_id))
            print('第{0}条用例执行结果：{1}'.format(case.case_id, resp.text))
            raise e


