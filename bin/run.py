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

run_args = [
    setting.TEST_PATH,
    '--reruns', '3',  # 用例失败则重试 3 次
    '--html=%s' % report,
]

pytest.main(run_args)

# subprocess.run(cmd)

# pre.stop_appium()