import unittest
from appium import webdriver
from time import sleep

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'DU2SSE15C3115777'
        desired_caps['appPackage'] = 'com.tencent.mm'#'com.android.contacts'
        desired_caps['appActivity'] = '.ui.LauncherUI'#'.activities.DialtactsActivity'
        desired_caps['unicodekeybord'] = 'True'
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # def getsize(self):
    #     x = self.driver.get_window_size()['width']
    #     y = self.driver.get_window_size()['height']
    #     return x, y
    def test_something(self):
        sleep(10)
        self.driver.wait_activity('.ui.LauncherUI',10,2)
        try:
            self.driver.find_element_by_name('通讯录').click()
            sleep(1)
            # self.getsize()   调用获取到的屏幕尺寸
            # K = self.getsize()
            # x1 = int(K[0] * 0.5)
            # y1 = int(K[1] * 0.75)
            # y2 = int(K[1] * 0.05)
            # self.driver.swipe(x1, y1, x1, y2)
            # sleep(2)
            self.driver.find_element_by_name('Duang').click()
            sleep(2)
            self.driver.find_element_by_id('com.tencent.mm:id/ahq').click()
            sleep(2)
            # x = self.driver.get_window_size()['width']
            # y = self.driver.get_window_size()['height']
            # return x,y
            # x=501
            # y=1701
            # sleep(1)
            self.driver.find_element_by_id('a71').click()
            sleep(2)
            self.driver.find_element_by_id('a71').send_keys(u'qichuangle')
            sleep(2)
            self.driver.find_element_by_name('发送').click()
            # self.driver.background_app(5)
            sleep(2)
            self.driver.close_app()
            self.driver.launch_app()
            sleep(3)
        except Exception as e:
            print(e)
    def test_wec(self):
        count =0
        counter=3
        while(count<counter):
            """11111112222222222"""
            self.test_something()
            count +=1
            print('正在进行第%s次发送消息'%count)
    @classmethod
    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     suit =unittest.TestSuite()
#     suit.addTest(MyTestCase('test_something'),MyTestCase('test_wec'))
#     runner =unittest.TextTestRunner(verbosity=3)
#     runner.run(suit)
