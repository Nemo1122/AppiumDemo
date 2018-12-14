import unittest
import setting
from appium import webdriver
from lib.prepare import  pre
from lib.utils import log
from page.public import Public
from page.my_center import MyCenter
from page.category import CategoryPage
from page.login import Login
from lib.uioperation import UiOperation


class Base(unittest.TestCase):

    driver = webdriver.Remote(setting.REMOTE_URL % setting.APORT,
                              setting.DESIRED_CAPABILITIES)
    ui = UiOperation(driver)

    def setUp(self):
        # 所有用例的起点为首页
        self.ui.start_page(activity='.activity.EcmobileMainActivity')

    def tearDown(self):
        # 测试用例完后，重置 app
        self.ui.reset()


