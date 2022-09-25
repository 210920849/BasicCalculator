import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from common import config
from page.loc_calculator import First_number, Second_number, Calculator, Answer, Operation, promot_message

class Testconculator(unittest.TestCase):
    def setUp(self):
        """每条用例执行前，都要先进入计算器页面"""
        self.dr = WebDriver()
        self.dr.get(config.HOST)     #打开浏览器
        self.dr.implicitly_wait(2)

    def tearDown(self):
        """每条用例执行后，都要退出浏览器"""
        self.dr.quit()


    def test1_add_conculator_suc(self):       #有效的加法计算
        self.dr.find_element(*First_number).send_keys(2)  #第一个数字输入2
        self.dr.find_element(*Second_number).send_keys(3) #第二个数字输入3
        self.dr.find_element(*Calculator).click()         #点击计算
        self.assertEqual('5',self.dr.find_element(*Answer).get_attribute('value'))  #断言


    def test11_divide_conculator_fail(self):      #无效的除法计算
        self.dr.find_element(*First_number).send_keys(1)  #第一个数字输入1
        self.dr.find_element(*Second_number).send_keys(0) #第二个数字输入0
        Select(self.dr.find_element(*Operation)).select_by_value("3") #选择除法
        self.dr.find_element(*Calculator).click()            #点击计算
        self.assertEqual('Divide by zero error!', self.dr.find_element(*promot_message).text) #断言


if __name__ == '__main__':
    unittest.main()