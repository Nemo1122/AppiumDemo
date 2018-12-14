from page.public import Public
from page.my_center import MyCenter
from page.category import CategoryPage
from page.login import Login
from page.setting_page import Setting
from page.product_detail import ProductDetail
from page.cart import Cart
from page.checkout import Checkout
from lib.utils import log
from testcase.base import Base


class TestOrder(Base):

    def test_order(self):
        # 点击个人中心
        self.ui.find(Public.ANDROID_MY_CENTER_BUTTON).click()
        # 点击登录
        self.ui.find(MyCenter.IN_LOGIN_BUTTON).click()
        # 输入用户名
        self.ui.find(Login.ANDROID_USERNAME).send_keys('nemo')
        # 输入密码
        self.ui.find(Login.ANDROID_PASSWORD).send_keys('asdf1234')
        # 点击登录按钮
        self.ui.find(Login.LOGIN_BUTTON).click()
        # 进入分类页
        self.ui.find(Public.ANDROID_CATEGORY_SEARCH_BUTTON).click()
        # 选择 “女装”分类
        self.ui.find(CategoryPage.CATEGORY_1).click()
        # 选择 “衬衫”分类
        self.ui.find(CategoryPage.CATEGORY_2).click()
        # 点击商品
        self.ui.find(CategoryPage.ANDROID_PRODUCT_1).click()
        # 记录当前商品价格
        price = self.ui.find(ProductDetail.ANDROID_PRICE).text
        log.info(price)
        # 加入购物车
        self.ui.find(ProductDetail.ADD_CART).click()
        # 查看购物车
        self.ui.find(ProductDetail.ANDROID_CART).click()
        # 进入结算中心
        self.ui.find(Cart.CHECKOUT_BUTTON).click()
        # 选择支付方式
        self.ui.find(Checkout.MODE_OF_PAY).click()
        self.ui.find(Checkout.ALI_PAY).click()
        # 选择配送方式
        self.ui.find(Checkout.MODE_OF_DELIVERY).click()
        self.ui.find(Checkout.PICK_UP_FROM_PATRON).click()
        # 提交订单
        self.ui.find(Checkout.SUBMIT_ORDER_BUTTON).click()
        # 取消立即支付
        self.ui.find(Checkout.ANDROID_CANCEL_BUTTON).click()
