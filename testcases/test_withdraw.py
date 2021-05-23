
import unittest
from common.do_excel import DoExcel
from common.request import Request
from common import contants
from ddt import ddt, data


@ddt()
class TestWithdraw(unittest.TestCase):
    """提现"""
    do_excel = DoExcel(contants.data_path, 'withdraw')
    cases = do_excel.raed()

    @classmethod
    def setUpClass(cls):
        cls.request = Request()

    @data(*cases)
    def test_withdraw(self, case):
        resp = self.request.request(case.method, case.url, case.date)
        try:
            print('第{0}条用例开始执行！'.format(case.case_id))
            self.assertEqual(str(case.expected), resp.json()['code'])
            self.do_excel.write(case.case_id+1, resp.json()['code'], 'PASS')
        except AssertionError as e:
            self.do_excel.write(case.case_id + 1, resp.json()['code'], 'FAIL')
            raise e
        finally:
            print('第{0}条用例执行结果：{1}'.format(case.case_id, resp.text))

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()


