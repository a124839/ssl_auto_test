import time
import os
from selenium import webdriver
from config.setting import DRIVER_PATH, REPORT_PATH, IMAGE_PATH
from utils.logger import Logger

# 根据传入的参数选择浏览器的driver去打开对应的浏览器

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
FIREFOX_PATH = DRIVER_PATH + '\geckodriver.exe'
EDGE_PATH = DRIVER_PATH + '\msedgedriver.exe'

IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'edge': webdriver.Edge}
EXECUTABLE_PATH = {'firefox': FIREFOX_PATH, 'chrome': CHROMEDRIVER_PATH, 'edge': EDGE_PATH}

logger = Logger(logger="Browser").getlog()


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = IMAGE_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        try:
            screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
            logger.info("页面已截图，截图的路径在项目: %s\%s_%s.png" % (screenshot_path, name, tm))
        except Exception as e:
            logger.error("失败截图 %s" % e)

    # def get_screen_image(self, image_name):
    #     screen_image = IMAGE_PATH + image_name + '.png'
    #     try:
    #         self.driver.get_screenshot_as_file(screen_image)
    #         logger.info("页面已截图，截图的路径在项目: %s " % IMAGE_PATH)
    #     except NameError as ne:
    #         logger.error("失败截图 %s" % ne)
    #         raise

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


# 这里试验了一下保存截图的方法，保存png截图到report目录下。
if __name__ == '__main__':
    b = Browser('firefox').get('http://www.baidu.com')

    time.sleep(3)
    b.save_screen_shot()
    b.quit()
