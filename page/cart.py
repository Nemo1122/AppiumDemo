from appium.webdriver.common.mobileby import MobileBy as by


class Cart:

    ANDROID_PRODUCT_NAME = by.ID, 'com.insthub.ecmobile:id/shop_car_item_text'
    ANDROID_PRICE = by.ID, 'com.insthub.ecmobile:id/shop_car_footer_total'

    CHECKOUT_BUTTON = '结算'
