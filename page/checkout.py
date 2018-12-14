from appium.webdriver.common.mobileby import MobileBy as by


class Checkout:

    MODE_OF_PAY = '支付方式'
    MODE_OF_DELIVERY = '配送方式'

    # ----------支付方式选择-------------
    ALI_PAY = '支付宝'
    # ----------配送方式选择-------------
    PICK_UP_FROM_PATRON = '上门取货'

    SUBMIT_ORDER_BUTTON = '提交订单'

    # ----------是否马上支付弹窗---------
    ANDROID_CONFIRM_BUTTON = by.ID, 'com.insthub.ecmobile:id/yes'
    ANDROID_CANCEL_BUTTON = by.ID, 'com.insthub.ecmobile:id/no'
