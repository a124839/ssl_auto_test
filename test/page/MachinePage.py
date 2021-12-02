from test.page.BasePage import BasePage
from selenium.webdriver.common.by import By
from test.common.ClickInto import ClickInto


class MachinePage(BasePage):
    left_device_manage = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/a[2]/div")
    left_sec_device_self_check = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[2]/li[1]/a")
    left_sec_device_backup = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[2]/li[2]/a")
    left_sec_backup_recover = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[2]/li[3]/a")
    left_sec_reset = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[2]/li[4]/a")
    left_sec_upgrade = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[2]/li[5]/a")
    # left_sec_device_backup = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[2]/li[6]/a")
    # 所有二级侧边栏中的右侧页面中的“确定”按钮xpath相同，css相同
    right_ok_btn = (By.CSS_SELECTOR, ".button2")
    right_backup_recover_path = (By.ID, "resu_file")
    device_self_chceck_res_window_close_btn = (By.XPATH, "/html/body/div[2]/div[3]/a/span/span[2]")

    iframe_father = (By.XPATH, "/html/body/div[2]/div[2]/div/div[2]")
    iframe_css = (By.CSS_SELECTOR, "#mainid > iframe:nth-child(1)")

    def device_self_check(self):
        # 点击设备自检
        self.click_sec_left(self.left_device_manage, self.left_sec_device_self_check)
        # 转为iframe
        self.switch_to_frame(self.find_element(self.iframe_css))
        # # 定位元素位置
        self.find_element(self.right_ok_btn).click()
        # 关闭弹框
        self.find_element(self.device_self_chceck_res_window_close_btn).click()

    def device_backup(self):
        # 点击设备备份
        self.click_sec_left(self.left_device_manage, self.left_sec_device_backup)
        # iframe父级
        self.find_element(self.iframe_father)
        # 转为iframe
        self.switch_to_frame(self.find_element(self.iframe_css))
        # # 定位元素位置
        self.find_element(self.right_ok_btn).click()
        # 关闭alert
        self.click_alert()

    def backup_recover(self, pkg_path):
        # 点击设备备份
        self.click_sec_left(self.left_device_manage, self.left_sec_backup_recover)
        # 转为iframe
        self.switch_to_frame(self.find_element(self.iframe_css))
        # 给定路径
        self.send_key(self.right_backup_recover_path, pkg_path)
        # 确定
        self.find_element(self.right_ok_btn).click()

    def device_reset(self):
        # 点击恢复出厂
        self.click_sec_left(self.left_device_manage, self.left_sec_reset)
        self.switch_to_frame(self.find_element(self.iframe_css))
        self.find_element(self.right_ok_btn).click()

    def device_upgrade(self):
        self.click_sec_left(self.left_device_manage, self.left_sec_upgrade)
        self.switch_to_frame(self.find_element(self.iframe_css))
        self.find_element(self.right_ok_btn).click()
        self.click_alert()
        # TODO:后续升级页面逻辑未编写


if __name__ == '__main__':
    mp = MachinePage('firefox')
    mp.get("http://192.168.1.111:7789/fortest?key=CN=admin,OU=XA,O=SDT,C=CN")
    # mp.device_backup()
    # mp.backup_recover("D:/")
    mp.device_upgrade()
