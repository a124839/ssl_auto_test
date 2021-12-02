from test.page.BasePage import BasePage
from selenium.webdriver.common.by import By

from test.common.ClickInto import ClickInto


class RunStatusPage(BasePage):
    left_run_status_menu = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/a[1]/div")
    left_sys_resource = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[1]/li[1]/a")
    left_user_connect = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[1]/li[2]/a")
    right_flush_status_btn = (By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/table[4]/tbody/tr/td/input")
    right_user_name = (By.XPATH,
                       "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div[1]/form/table/tbody/tr/td["
                       "2]/span[2]/input[1]")
    right_login_ip = (By.XPATH, '//*[@id="loginIP"]')
    right_search_btn = (
        By.XPATH,
        "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div[1]/form/table/tbody/tr/td[4]/a/span/span[2]")
    iframe_father = (By.XPATH, "/html/body/div[2]/div[2]/div/div[2]")
    iframe_css = (By.CSS_SELECTOR, "#mainid > iframe:nth-child(1)")

    def run_status_check(self):
        # 左边一级
        self.find_element(self.left_run_status_menu).click()
        # 左边二级
        self.find_element(self.left_sys_resource).click()

        # ClickInto.click_left(self.left_run_status_menu, self.left_sys_resource)

        # iframe父级
        self.find_element(self.iframe_father)
        # 转为iframe
        self.switch_to_frame(self.find_element(self.iframe_css))
        # 找到刷新按钮
        self.find_element(self.right_flush_status_btn).click()

        # TODO:判断页面是否刷新，或者请求返回码

    def user_connect_search(self, user_name="", login_ip=""):
        # 左边一级
        self.find_element(self.left_run_status_menu).click()
        # 左边二级
        self.find_element(self.left_user_connect).click()
        # iframe父级
        self.find_element(self.iframe_father)
        # 转为iframe
        self.switch_to_frame(self.find_element(self.iframe_css))
        # 判断
        if user_name == "" and login_ip == "":
            pass
        else:
            if user_name != "":
                # 根据用户名查询
                self.send_key(self.right_user_name, user_name)
            # 根据登录IP查询
            if login_ip != "":
                self.send_key(self.right_login_ip, login_ip)
            self.find_element(self.right_search_btn).click()


if __name__ == '__main__':
    rs = RunStatusPage("firefox")
    rs.get("http://192.168.1.111:7789/fortest?key=CN=admin,OU=XA,O=SDT,C=CN")
    # rs.run_status_check()
    rs.user_connect_search("aaa", "192.168.1.1")

    # rs.quit()
