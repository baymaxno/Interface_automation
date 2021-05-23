
import unittest
from common.do_excel import DoExcel
from common.request import Request
from common import contants
from ddt import ddt, data
from common.logger import Logging
import json


@ddt()
class TestLogin(unittest.TestCase):
    """登录"""

    do_excel = DoExcel(contants.data_path, 'login')
    cases = do_excel.raed()
    request = Request()

    @classmethod
    def setUpClass(cls):
        cls.logger = Logging('my_log')

    def setUp(self):
        pass

    @data(*cases)
    def test_login(self, case):
        headers = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
        resp = self.request.request(case.method, case.url, case.date, headers=headers)  # 调用接口
        resp_dice = json.loads(resp.text)
        try:
            self.logger.info('第{0}条用例开始执行！'.format(case.case_id), 'logger.log')
            print(resp_dice["msg"])
            self.assertEqual(case.expected, resp_dice["msg"])  # 断言
            self.do_excel.write(case.case_id+1, resp_dice["msg"], 'PASS')  # 写入结果
            self.logger.info('第{0}条用例执行结果：PASS'.format(case.case_id), 'logger.log')
        except AssertionError as e:
            self.do_excel.write(case.case_id+1, resp_dice["msg"], 'FAIL')
            self.logger.warning('第{0}条用例执行结果：FAIL'.format(case.case_id), 'logger.log')
            raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass