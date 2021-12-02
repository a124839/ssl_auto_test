from test.common.Browser import Browser
from config import setting
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from utils.logger import Logger
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

# 创建log实例
logger = Logger(logger="BasePage").getlog()


class BasePage(Browser):

    def get_page_title(self):
        return self.driver.title

    def find_element(self, loc):
        # return self.driver.find_element(*loc)
        try:
            # 元素可见时，返回查找元素，入参为元组的元素，需要加*
            # WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element(*loc).is_displayed())
            # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            # log
            logger.warning('找不到定位元素: %s ' % loc[1])
            raise
        except TimeoutException:
            # log
            logger.warning('查找元素超时: %s' % loc[1])
            raise

    def find_elements(self, loc):
        try:
            # 元素可见时，返回查找元素，入参为元组的元素，需要加*
            # WebDriverWait(self.driver, 30).until(lambda driver: self.driver.find_elements(*loc).is_displayed())
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            # log
            logger.warning('找不到定位元素: %s ' % loc[1])
            raise
        except TimeoutException:
            # log
            logger.warning('查找元素超时: %s' % loc[1])
            raise

    def send_key(self, loc, text):
        logger.info('清空文本框内容: ...' )
        self.find_element(loc).clear()
        time.sleep(1)
        # logger.info('输入内容的元素: %s...' % loc)
        logger.info('输入内容: %s' % text)
        try:
            self.driver.find_element(*loc).send_keys(text)
            time.sleep(1)
        except Exception as e:
            logger.error("输入内容失败 %s" % e)
            self.save_screen_shot(text)

    def click(self, loc):
        logger.info('点击元素 by %s: %s...' % (loc[0], loc[1]))
        try:
            self.find_element(loc).click()
            time.sleep(2)
        except AttributeError as e:
            logger.error("无法点击元素: %s" % e)
            raise

    # 切换frame页面
    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    # 切换alter
    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def clear(self, loc):
        '''输入文本框清空操作'''
        element = self.find_element(loc)
        try:
            element.clear()
            logger.info('清空文本框内容')
        except NameError as ne:
            logger.error("清空文本框内容失败: %s" % ne)
            self.save_screen_shot(ne)

        '''
        鼠标悬停操作
        Usage:
        element = ("id","xxx")
        driver.move_to_element(element)
        '''

    def move_to_element(self, loc):
        ele = self.driver.find_element(*loc)
        ActionChains(self.driver).move_to_element(ele).perform()

    def back(self):
        """
        浏览器返回窗口
        """
        self.driver.back()
        logger.info('返回上一个页面')

    def forward(self):
        """
        浏览器前进下一个窗口
        """
        self.driver.forward()
        logger.info('前进到下一个页面')

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒" % seconds)

    def close(self):
        """
        关闭浏览器
        """
        try:
            self.driver.close()
            logger.info('关闭浏览器窗口')
        except NameError as ne:
            logger.error("关闭浏览器窗口失败 %s" % ne)

    def quit(self):
        """
        退出浏览器
        """
        self.driver.quit()

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, loc):
        '''获取文本'''
        element = self.find_element(loc)
        return element.text

    def get_attribute(self, loc, name):
        '''获取属性'''
        element = self.find_element(loc)
        return element.get_attribute(name)

    def js_execute(self, js):
        '''执行js'''
        return self.driver.execute_script(js)

    def js_focus_element(self, loc):
        '''聚焦元素'''
        target = self.find_element(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, loc, index):
        '''通过索引,index是索引第几个，从0开始'''
        ele = self.find_element(loc)
        Select(ele).select_by_index(index)

    def select_by_value(self, loc, value):
        '''通过value属性'''
        element = self.find_element(loc)
        Select(element).select_by_value(value)

    def select_by_text(self, loc, text):
        '''通过文本值定位'''
        element = self.find_element(loc)
        Select(element).select_by_value(text)

    def is_text_in_element(self, loc, text, timeout=10):
        """判断文本在元素里，没定位到元素返回False，定位到元素返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(loc, text))
        except TimeoutException:
            logger.warning('元素没有定位到:' + str(loc))
            return False
        else:
            return True

    def is_text_in_value(self, loc, value, timeout=10):
        '''
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(element, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element_value(loc, value))
        except TimeoutException:
            logger.warning('元素没有定位到:' + str(loc))
            return False
        else:
            return True

    def is_title(self, title, timeout=10):
        '''判断title完全等于'''
        res = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return res

    def is_title_contains(self, title, timeout=10):
        '''判断title包含'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, loc, timeout=10):
        '''判断元素被选中，返回布尔值,'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(loc))
        return result

    def is_selected_be(self, loc, selected=True, timeout=10):
        '''判断元素的状态，selected是期望的参数true/False
        返回布尔值'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_selection_state_to_be(loc, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''判断页面是否有alert，
        有返回alert(注意这里是返回alert,不是True)
        没有返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, loc, timeout=10):
        '''元素可见返回本身，不可见返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(loc))
        return result

    def is_invisibility(self, loc, timeout=10):
        '''元素可见返回本身，不可见返回True，没找到元素也返回True'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.invisibility_of_element_located(loc))
        return result

    def is_clickable(self, loc, timeout=10):
        '''元素可以点击is_enabled返回本身，不可点击返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(loc))
        return result

    def is_located(self, loc, timeout=10):
        '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(loc))
        return result

    def click_alert(self):
        '''操作点击弹窗'''
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)

    def alert_text(self):
        '''返回弹窗的文本内容'''
        alert = self.driver.switch_to.alert()
        rel = alert.text()
        return rel

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

    # def switch_to_window(self, loc):
    #     self.driver.find_element(loc).text
