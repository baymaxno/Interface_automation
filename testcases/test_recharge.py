
import unittest
from common.do_excel import DoExcel
from common.request import Request
from common import contants
from ddt import ddt, data

'''
1.设计用例的时候，先设计一条正常登陆的用例
2.利用session.request的方法保存登陆的会话
3.
'''


@ddt()
class TestRecharge(unittest.TestCase):
    """充值"""

    do_excel = DoExcel(contants.data_path, 'recharge')
    cases = do_excel.raed()

    @classmethod
    def setUpClass(cls):  # 类方法，整个类只执行一次
        cls.request = Request()

    def setUp(self):  # setUp方法，实例化一次test_recharge用例一次就执行一次
        print('-------------用例执行开始------------')

    @data(*cases)
    def test_recharge(self, case):
        headers = {"X-Lemonban-Media-Type": "lemonban.v1",
                   "Content-Type": "application/json"
                   }

        resp = self.request.request(case.method, case.url, case.date, headers=headers)  # 调用接口
        try:
            print('第{0}条用例开始执行！'.format(case.case_id))
            self.assertEqual(str(case.expected), resp.json()['msg'])  # 断言
            self.do_excel.write(case.case_id+1, resp.json()['msg'], 'PASS')  # 写入结果
            print('第{0}条用例执行结果：{1}'.format(case.case_id, resp.text))
        except AssertionError as e:
            self.do_excel.write(case.case_id+1, resp.json()['msg'], 'FAIL')
            print('第{0}条用例执行结果：{1}'.format(case.case_id, resp.text))
            raise e

    def tearDown(self):
        print('-------------用例执行结束------------')

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
