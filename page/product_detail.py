from appium.webdriver.common.mobileby import MobileBy as by


class ProductDetail:

    # -----------价格------------
    ANDROID_PRICE = by.ID, 'com.insthub.ecmobile:id/good_property'

    # -----------底部按钮---------
    ADD_CART = '加入购物车'
    FAST_BUY = '快速购买'
    ANDROID_CART = by.ID, 'com.insthub.ecmobile:id/good_detail_shopping_cart'

