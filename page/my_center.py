from appium.webdriver.common.mobileby import MobileBy as by
"""
页面元素命名规范：
1. 元素名称必须大写;
2. 必须以与元素业务相关的英文单词及单词组合命名, 多个单词以下划线分隔;
3. 如果该元素已有命名, 则以已有命名为主, 一般出现在 id 中;
4. 命名结尾根据元素的特征标识：
    CLK(可点击), TXT(获取文本), IMG(获取图片), CHK(复选框), RDO(单选), SLT(下拉菜单), OPT(下拉选项), TST(提示)
    PGB(进度条);
5. 如该定位仅 Android 能用, 则以大写的 ANDROID 开头, 若仅 iOS 能用则以大写的 IOS 开头;
6. 可以直接以可见文本定位的元素, 直接以文本(或部分文本)为定位语句, 不需要加定位方式( Android 的 text 属性或者 iOS 的 name 属性);
7. 不能以可见文本定位的元素, 必须加上定位方式和定位语句。

示例：
如'个人中心'设置按钮, 其 id 为'com.insthub.ecmobile:id/profile_setting' 可命名为 PROFILE_SETTING_CLK, 又因 id 定位只有
Android 支持, 因此前面加上 ANDROID。则完整命名为： "ANDROID_PROFILE_SETTING_CLK"

注：每个页面类上必须加上本规范文字！
"""


class MyCenter:
    # 顶部设置按钮
    ANDROID_PROFILE_SETTING_CLK = by.ID, 'com.insthub.ecmobile:id/profile_setting'

    IN_LOGIN_CLK = '点击此处登录'
    WAIT_FOR_PAY_CLK = '待付款'
    WAIT_FOR_SEND_CLK = '待发货'
    WAIT_FOR_RECEIVE_CLK = '待收货'
    HISTORY_ORDER_CLK = '历史订单'

    MY_FAVORITE_CLK = '我的收藏'
    MANAGE_ADDRESS_CLK = '收货地址管理'
    HELP_CLK = '帮助'

    # -----------------登录的页面元素----------------
    ANDROID_USER_NAME_TXT = by.ID, 'com.insthub.ecmobile:id/profile_head_name'
    ANDROID_USER_LEVEL_TXT = by.ID, 'com.insthub.ecmobile:id/member_level'




