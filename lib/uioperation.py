import setting
import time
import os
from appium import webdriver
from lib.utils import wait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class UiOperation():
    def __init__(self, driver):
        self.driver = driver
        self.desired_capabilities = self.driver.desired_capabilities
        self.package = self.desired_capabilities['appPackage']
        self.lunch_activity = self.desired_capabilities['appActivity']
        self.platform = self.desired_capabilities['platformName']
        # self.driver = webdriver.Remote(setting.REMOTE_URL % 4723, caps)

    # 封装定位方法
    @wait()
    def find(self, locator, ios=None):
        """
        封装 Appium 定位方法
        :param locator: 可见文本或者其他的定位方式
        :param ios: 同一个控件，IOS 和 Android 分别使用不同的定位方式则为该参数赋值
        :return: 元素对象
        """
        # 如果传入字符串，则使用文本定位的方式
        if isinstance(locator, str):
            if self.platform == 'Android':
                try:
                    # uiautomator
                    element = self.driver.find_element_by_android_uiautomator(
                        'new UiSelector().text("%s")' % locator)
                except NoSuchElementException:
                    element = self.driver.find_element_by_android_uiautomator(
                        'new UiSelector().textContains("%s")' % locator)
            else:
                try:
                    # name, label
                    element = self.driver.find_element_by_accessibility_id(locator)
                except NoSuchElementException:
                    # name CONTAINS 'testcase'
                    element = self.driver.find_element_by_ios_predicate("name CONTAINS '%s'" % locator)
        else:
            if self.platform == 'Android':
                element = self.driver.find_element(*locator)
            else:
                element = self.driver.find_element(*ios)
        return element

    # 封装直接跳转某页面的方法
    def start_page(self, activity=None, package=None):
        package = package if package else self.package
        activity = activity if activity else self.lunch_activity

        self.driver.start_activity(package, activity)

    def swipe(self, sx, sy, ex, ey, duration=300):
        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        self.driver.swipe(sx*x, sy*y, ex*x, ey*y, duration=duration)

    def swipe_left(self):
        self.swipe(0.8, 0.5, 0.2, 0.5)
        time.sleep(1)

    def swipe_right(self):
        self.swipe(0.2, 0.5, 0.8, 0.5)
        time.sleep(1)

    def swipe_up(self):
        self.swipe(0.5, 0.8, 0.5, 0.2)
        time.sleep(1)

    def swipe_down(self):
        self.swipe(0.5, 0.2, 0.5, 0.8)
        time.sleep(1)

    def screen(self, filename):
        img = os.path.join(setting.IMG_PATH, time.strftime('%Y%m%d%H%M%S_') + filename + '.png')
        print(img)
        self.driver.get_screenshot_as_file(img)

    # 重置 APP
    def reset(self):
        self.driver.reset()