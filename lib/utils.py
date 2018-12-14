import subprocess
import logging
import os
import time
from logging import handlers
import setting
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


def cmd(cmd):
    return subprocess.Popen(cmd, shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            bufsize=1)


def wait(poll=0.5, message=''):
    def decorator(method):
        def wrapper(self, *args, **kw):
            end_time = time.time() + setting.WAIT_TIME_OUT
            while True:
                try:
                    return method(self, *args, **kw)
                except NoSuchElementException as exc:
                    screen = getattr(exc, 'screen', None)
                    stacktrace = getattr(exc, 'stacktrace', None)
                time.sleep(poll)
                if time.time() > end_time:
                    break
            raise TimeoutException(message, screen, stacktrace)
        return wrapper
    return decorator


def screen_when_err(func):
    def wrapper(self, *args, **kw):
        try:
            # 捕获函数异常
            return func(self, *args, **kw)
        except Exception:
            # 函数出现异常后的处理
            self.ui.screen(func.__name__+'_err', path=setting.ERR_IMG_PATH)
            # 为了能在结果展示异常，需要重新抛出该异常
            raise
    return wrapper


class MyLogger(object):
    def __init__(self,file_name,level='info',backCount=5,when='D'):
        logger = logging.getLogger()
        logger.setLevel(self.get_level(level))  # 设置日志的级别
        # fl = logging.FileHandler(filename='a.log', mode='a', encoding='utf-8')
        cl = logging.StreamHandler()  # 负责往控制台输出的
        bl = handlers.TimedRotatingFileHandler(filename=file_name, when=when, interval=1,
                                               backupCount=backCount, encoding='utf-8')
        fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d]-%(levelname)s:%(message)s')
        # 指定日志的格式
        cl.setFormatter(fmt)  # 设置控制台输出的日志格式
        bl.setFormatter(fmt)  # 设置文件里面写入的日志格式
        logger.addHandler(cl)  # 把已经设置好的人放到办公室中
        logger.addHandler(bl)  # 同上
        self.logger = logger

    def get_level(self, sss):
        level = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warn': logging.WARN,
            'error': logging.ERROR
        }
        sss = sss.lower()
        return level.get(sss)


path = os.path.join(setting.LOG_PATH,  setting.LOG_NAME)  # 拼好日志的绝对路径
log = MyLogger(path, setting.LOG_LEVEL).logger