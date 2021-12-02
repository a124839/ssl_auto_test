from test.page.BasePage import BasePage
from selenium.webdriver.common.by import By


class ClickInto(BasePage):

    iframe_father = (By.XPATH, "/html/body/div[2]/div[2]/div/div[2]")
    iframe_css = (By.CSS_SELECTOR, "#mainid > iframe:nth-child(1)")

    def click_sec_left(self, left_1, left_2=None):
        '''
        实现点击左侧栏动作
        :param left_1:
        :param left_2:
        :return: webelement
        '''
        if left_2 is None:
            return self.find_element(left_1).click()
        else:
            self.find_element(left_1).click()
            return self.find_element(left_2).click()

    def change_to_right(self):
        '''
        仅实现从左侧标题栏切换到右侧iframe操作
        :return: 右侧webElement
        '''
        # iframe父级
        self.find_element(self.iframe_father)
        # 转为iframe
        return self.switch_to_frame(self.find_element(self.iframe_css))


