import unittest
from XTestRunner import HTMLTestRunner
from XTestRunner import label


class TestDemo(unittest.TestCase):
    """测试用例说明"""

    def test_success(self):
        """执行成功"""
        print('1111111')

    @unittest.skip("skip case")
    def test_skip(self):
        pass

    def test_fail(self):
        print('1111111')

    def test_error(self):
        print('1111111')


class TestDemo2(unittest.TestCase):

    def test_success(self):
        print('1111111')


class TestDemo3(unittest.TestCase):

    @label("fail")
    def test_fail(self):
        print('1111111')


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestDemo("test_success"))
    suit.addTest(TestDemo("test_skip"))
    suit.addTest(TestDemo("test_fail"))
    suit.addTest(TestDemo("test_error"))
    suit.addTest(TestDemo2("test_success"))
    suit.addTest(TestDemo3("test_fail"))

    with(open('./reports/result.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<project name>test report',
            description='describe: ... ',
            language='en',
            blacklist=["fail"],
        )
        runner.run(suit)