import os
from lib import utils

class ADB:
    def connect(self, url):
        cmd = 'adb connect %s' % url
        return utils.cmd(cmd)

    def get_devices(self):
        devices_list = []
        devices = str(utils.cmd('adb devices').stdout.read(), 'utf-8')
        for device in devices.splitlines()[1:]:
            if 'device' in device:
                device = device.split('\t')[0]
                devices_list.append(device)
        return devices_list

    def stop_adb(self):
        cmd = 'adb kill-server'
        utils.cmd(cmd)

    def start_adb(self):
        cmd = 'adb start-server'
        if 'successfully' not in utils.cmd(cmd).stdout.readline():
            raise ConnectionError('adb 启动失败，请检查 5037 端口是否被占用！')

adb = ADB()