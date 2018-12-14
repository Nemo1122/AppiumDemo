from appium.webdriver.common.mobileby import MobileBy as by


class Setting:

    LOGOUT = '注销'

    # ----------退出弹框-----
    CONFIRM_BUTTON = by.ID, 'com.insthub.ecmobile:id/yes'
    CANCEL_BUTTON = by.ID, 'com.insthub.ecmobile:id/no'