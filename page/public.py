from appium.webdriver.common.mobileby import MobileBy as by


class Public:
    """
    公共按钮
    """
    # 下方菜单栏
    ANDROID_HOME_BUTTON = by.ID, 'com.insthub.ecmobile:id/toolbar_tabone'
    ANDROID_CATEGORY_SEARCH_BUTTON = by.ID, 'com.insthub.ecmobile:id/toolbar_tabtwo'
    ANDROID_CART_BUTTON = by.ID, 'com.insthub.ecmobile:id/toolbar_tabthree'
    ANDROID_MY_CENTER_BUTTON = by.ID, 'com.insthub.ecmobile:id/toolbar_tabfour'



