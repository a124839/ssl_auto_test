import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import HTMLTestRunner
from config.setting import REPORT_PATH,FIREFOX_PATH,CHROME_PATH
import os
import time

import selenium.webdriver.support.ui as ui


class s02(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        print("222up--")
        cls.driver = webdriver.Firefox(executable_path=FIREFOX_PATH)
        # cls.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        cls.driver.get("http://192.168.1.111:7789/fortest?key=CN=admin,OU=XA,O=SDT,C=CN")
    '''
    def testT1(self):
        # self.driver.find_element(By.ID, "J_search_input").send_keys("电动自行车")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/a[1]/div").click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,"//*[@id='firstpane']/ul[1]/li[1]/a").click()

        self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div/ul[1]/li[1]/a").click()# 火狐浏览器中可以用
        # self.driver.find_element(By.XPATH,"//*[@id='form1']/div/table/tbody/tr[2]/td/table[4]/tbody/tr/td/input").click()
        print("==2222exe==")
    '''
    def testT2(self):
        a = (By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div/a[2]/div")
        print(" aa  %s %s " %(a[0], a[1]))
        # 设备管理
        self.driver.find_element(a[0],a[1]).click()
        # 设备自检
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div/ul[2]/li[1]/a").click()
        # 点击确定
        # 找到父级元素 class=“rightMenu”
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]")
        # 切换到iframe
        iframe = self.driver.find_element(By.CSS_SELECTOR,"#mainid > iframe:nth-child(1)")
        self.driver.switch_to.frame(iframe)
        # 定位元素位置
        self.driver.find_element(By.CSS_SELECTOR,".button2").click()
        # 弹框
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/a/span").click()
        time.sleep(3)
        info = self.driver.switch_to.alert
        print(info.text)
        info.dismiss()
        print("--设备自检--")
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        print("---22donw")


if __name__ == '__main__':
    tt = unittest.TestSuite()#创建测试套件
    # tt.addTests([s01("testT1"),s02("testT1")])
    tt.addTest(unittest.makeSuite(s02))
    # print("tt的类型为 %s" %tt)

    fp = open(os.path.join(REPORT_PATH,"report.html"),"w")
    rr = HTMLTestRunner.HTMLTestRunner(stream=fp, title="s01s02测试报告",description="用例情况")
    rr.run(tt)
    fp.close()


