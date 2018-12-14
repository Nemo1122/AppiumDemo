from appium.webdriver.common.mobileby import MobileBy as by


class CategoryPage:

    # 顶部搜索按钮
    ANDROID_SEARCH_BUTTON = by.ID, 'com.insthub.ecmobile:id/search_input'
    ANDROID_VOICE_SEARCH_BUTTON = by.ID, 'com.insthub.ecmobile:id/search_voice'

    # 女装分类
    CATEGORY_1 = '女装'
    CATEGORY_2 = '衬衫'

    # 商品
    ANDROID_PRODUCT_1 = by.XPATH, '//*[contains(@text, "韩味HW-2014")]/preceding-sibling::*'