from appium.webdriver.common.mobileby import MobileBy as by


class Login:

    ANDROID_USERNAME = by.ID, 'com.insthub.ecmobile:id/login_name1'
    ANDROID_PASSWORD = by.ID, 'com.insthub.ecmobile:id/login_password'

    LOGIN_BUTTON = '登录'
