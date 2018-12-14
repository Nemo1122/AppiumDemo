from lib import prepare
import sys
import os

path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(path)

import pytest
import setting
from lib.prepare import pre
import subprocess

# pre.start_appium('127.0.0.1:21503')

# cmd = 'pytest {test_path}  --reruns 3 --reruns-delay 1 -n 3 --alluredir {report_path}'.format(
report = os.path.join(setting.HTML_PATH, 'report.html')
allure_results = os.path.join(setting.REPORT_PATH, 'allure', 'results_data')
allure_report = os.path.join(setting.REPORT_PATH, 'allure', 'report')

run_args = [
    setting.TEST_PATH,
    '--reruns', '3',  # 用例失败则重试 3 次
    '--alluredir', allure_results,
]

pytest.main(run_args)

# 生成 allure 测试报告
allure_command = os.path.join(setting.ALLURE_PATH, 'allure')
cmd = '{allure_path} generate {allure_results} -o {allure_report}'.format(
    allure_path=allure_command,
    allure_results=allure_results,
    allure_report=allure_report
)
os.system(cmd)

# subprocess.run(cmd)

# pre.stop_appium()