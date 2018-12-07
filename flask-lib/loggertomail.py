# -*- coding:utf-8 -*-
'''
按级别分类日志器
按[debug]、[info]、[warn]、[error]及以下 四个级别分类
对存放在logs文件夹下文件名log_debug、log_info、log_warn、log_error
日志格式[2018/12/07 14:08:48] [INFO] [D:\Python36\lib\site-packages\werkzeug\_internal.py:88] [ * Running on http://0.0.0.0:5003/ (Press CTRL+C to quit)]
单个日志大小100M，最多存放10个回滚
error级别自动发送警告邮件（需配置邮箱及smtp），同步timeout1秒

'''
import logging
from logging.handlers import RotatingFileHandler, SMTPHandler


def setup_log():
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    file_log_handler_info = RotatingFileHandler("logs/log_info", maxBytes=1024 * 1024 * 100, backupCount=10,
                                                encoding='utf-8')
    file_log_handler_info.setLevel(logging.INFO)

    file_log_handler_debug = RotatingFileHandler("logs/log_debug", maxBytes=1024 * 1024 * 100, backupCount=10,
                                                 encoding='utf-8')
    file_log_handler_debug.setLevel(logging.DEBUG)

    file_log_handler_error = RotatingFileHandler("logs/log_error", maxBytes=1024 * 1024 * 100, backupCount=10,
                                                 encoding='utf-8')
    file_log_handler_error.setLevel(logging.ERROR)

    file_log_handler_warn = RotatingFileHandler("logs/log_warn", maxBytes=1024 * 1024 * 100, backupCount=10,
                                                encoding='utf-8')
    file_log_handler_warn.setLevel(logging.WARN)

    # INFO,DEBUG,WARN 仅监控对应级别， ERROR向下监控所有级别
    filter_info = LogLevelFilter(level=logging.INFO)
    filter_debug = LogLevelFilter(level=logging.DEBUG)
    filter_warn = LogLevelFilter(level=logging.WARN)

    file_log_handler_info.addFilter(filter_info)
    file_log_handler_debug.addFilter(filter_debug)
    file_log_handler_warn.addFilter(filter_warn)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(pathname)s:%(lineno)d] [%(message)s]',
                                  datefmt='%Y/%m/%d %H:%M:%S')
    file_log_handler_debug.setFormatter(formatter)
    file_log_handler_error.setFormatter(formatter)
    file_log_handler_info.setFormatter(formatter)
    file_log_handler_warn.setFormatter(formatter)

    # smtp.exmail.qq.com(使用SSL，端口号465)
    mail_handler = SMTPHandler(mailhost=("smtp.163.com", 25), # 163
                               fromaddr='18601776432@163.com',
                               toaddrs=['kongnanfei@hmdata.com.cn'],
                               subject="Warnning log",
                               credentials=('username', 'password'),
                               timeout=1.0
                               )
    mail_handler.setLevel(logging.ERROR)

    logger.addHandler(file_log_handler_info)
    logger.addHandler(file_log_handler_debug)
    logger.addHandler(file_log_handler_warn)
    logger.addHandler(file_log_handler_error)
    logger.addHandler(mail_handler)
    return logger


class LogLevelFilter(logging.Filter):

    def __init__(self, name='', level=logging.DEBUG):
        super(LogLevelFilter, self).__init__(name)
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
'''

if __name__ == '__main__':
    logger = setup_log()
    logger.debug('for debug')
    logger.error('for error')
    logger.fatal('for FATAL')
