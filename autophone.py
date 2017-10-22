#couding =unf-8
from time import sleep
from appium import webdriver
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'DU2SSE15C3115777'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.DialtactsActivity'
        # desired_caps['unicodekeybord'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def test_process(self):
        # sleep(2)
        # self.driver.wait_activity('.activities.DialtactsActivity',5,2)
        try:
            self.driver.find_element_by_id('call_log_list_item_time_axis_child_content').click()
            sleep(3)
            self.driver.find_element_by_name('挂断').click()
            sleep(2)
            self.driver.close_app()
            self.driver.launch_app()
        except Exception as e:
            print(e)
            print('pass')

    def test_wec(self):
        count = 0
        counter = 3
        while (count < counter):
            self.test_process()
            count += 1
            print('正在进行第%s次打电话' % count)
    def test_something(self):
        self.driver.quit()


if __name__ == '__main__':
    suit =unittest.TestSuite()
    suit.addTest(MyTestCase('test_wec'))
    suit.addTest(MyTestCase('test_wec'))
    runner =unittest.TextTestRunner(verbosity=2)
    runner.run(suit)