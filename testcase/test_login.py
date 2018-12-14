import pytest
from page.public import Public
from page.my_center import MyCenter
from page.login import Login
from page.setting_page import Setting
from lib.utils import log
from testcase.base import Base
import unittest


class TestLogin(Base):

    # @pytest.mark.skip()
    def test_login(self):
        # 点击个人中心
        self.ui.find(Public.ANDROID_MY_CENTER_BUTTON).click()
        # 点击登录
        self.ui.find(MyCenter.IN_LOGIN_CLK).click()
        # 输入用户名
        self.ui.find(Login.ANDROID_USERNAME).send_keys('nemo')
        # 输入密码
        self.ui.find(Login.ANDROID_PASSWORD).send_keys('asdf1234')
        # 点击登录按钮
        self.ui.find(Login.LOGIN_BUTTON).click()
        log.info('使用账号 [nemo] 和密码 [asdf1234] 登录！')
        # 检查个人中心
        username = self.ui.find(MyCenter.ANDROID_USER_NAME_TXT).text
        user_level = self.ui.find(MyCenter.ANDROID_USER_LEVEL_TXT).text

        self.assertEqual(username, 'nemo')
        self.assertEqual(user_level, 'vip')

    def tearDown(self):
        self.ui.find(MyCenter.ANDROID_PROFILE_SETTING_CLK).click()
        self.ui.find(Setting.LOGOUT).click()
        self.ui.find(Setting.CONFIRM_BUTTON).click()


if __name__ == '__main__':
    unittest.main()