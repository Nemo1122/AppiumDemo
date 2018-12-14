import os


# 目录
PATH = os.path.dirname(
    os.path.abspath(__file__)
)

REPORT_PATH = os.path.join(PATH, 'report')
HTML_PATH = os.path.join(REPORT_PATH, 'html')
IMG_PATH = os.path.join(REPORT_PATH, 'img')
LOG_PATH = os.path.join(REPORT_PATH, 'log')
TEST_PATH = os.path.join(PATH, 'testcase')
APP_PATH = os.path.join(PATH, 'app')
ERR_IMG_PATH = os.path.join(REPORT_PATH, 'err_img')

DESIRED_CAPABILITIES = {
    'deviceName': '192.168.199.101:5555',
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'appPackage': 'com.insthub.ecmobile',
    'appActivity': 'com.insthub.BeeFramework.activity.StartActivity',
    'App': os.path.join(APP_PATH, 'ECMobile3.2.apk'),
    'newCommandTimeout': 600,
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

# 显式等待时长
WAIT_TIME_OUT = 30

REMOTE_URL = 'http://localhost:%s/wd/hub'
APORT = 4723

# 日志
LOG_LEVEL = 'info'
LOG_NAME = 'log'

ALLURE_PATH = os.path.join(PATH, 'bin', 'allure-commandline', 'bin')

XYAZ = '127.0.0.1:21503'
