import time
import random
import re
from lib import utils
from lib.utils import  log
from lib.command import adb


class Prepare:

    def _connect_device(self, url=None):
        if url:
            adb.connect(url)
        while True:
            time.sleep(1)
            # 判断设备是否连上
            device = adb.get_devices()
            if device:
                log.info(device)
                print(device)
                return device

    def _appium_server_command(self, aport, bpport, device=None):
        if device:
            appium = utils.cmd("appium -p %s -bp %s -U %s" %
                        (aport, bpport, device))  # 启动appium
        else:
            appium = utils.cmd("appium -p %s -bp %s" %
                               (aport, bpport))  # 启动appium
        while True:
            appium_line = str(appium.stdout.readline(), 'utf-8').strip()
            log.debug(appium_line)
            time.sleep(1)
            if 'listener started' in appium_line or 'Error: listen' in appium_line:
                break

    def start_appium(self, url=None):

        aport = random.randint(4700, 4900)
        bpport = random.randint(4700, 4900)

        devices = self._connect_device(url)

        for device in devices:
            print(device)
            isVm = re.search(r'\d+\.\d+\.\d+\.\d+:\d+', device)

            if device and (not isVm):
                self._appium_server_command(aport, bpport, device)
                log.debug("appium -p %s -bp %s -U %s" %
                        (aport, bpport, device))
            elif device and isVm:
                self._appium_server_command(aport, bpport)
                log.debug("appium -p %s -bp %s" %
                          (aport, bpport))

        return aport

    def stop_appium(self):
        node = utils.cmd('tasklist | findstr node.exe').stdout.read()
        pid = [i for i in str(node, 'utf-8').split(' ') if i][1]

        utils.cmd('taskkill -f -pid %s' % pid)
        log.debug('stop appium')


pre = Prepare()
# import setting
# pre.start_appium(setting.XYAZ)
# pre.stop_appium()
# pre._connect_device('127.0.0.1:21503')