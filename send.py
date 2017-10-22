import unittest
from time import sleep
from wechat1 import MyTestCase
from HTMLTestRunner import HTMLTestRunner
if __name__ == '__main__':
    suit =unittest.TestSuite()
    x=[MyTestCase('test_something'), MyTestCase('test_wec')]
    suit.addTests(x)
    # suit.addTest(MyTestCase('test_something'),MyTestCase('test_wec'))
    runner = unittest.TextTestRunner(verbosity=2)
    print('test.html')
    f =open('test.html','wb'
            )
    runner =HTMLTestRunner(stream=f,
                           title='测试报告',
                           description='测试用例执行情况')

    runner.run(suit)

        # runner =unittest.TextTestRunner(verbosity=2)
        # f.write(suit)
        # runner.run(suit)