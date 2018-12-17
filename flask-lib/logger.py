# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

from flask import request


def setup_log():
    # os.mkdir("logs") if "logs" not in os.listdir() else None
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

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

    logger.addHandler(file_log_handler_info)
    logger.addHandler(file_log_handler_debug)
    logger.addHandler(file_log_handler_warn)
    logger.addHandler(file_log_handler_error)
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
    logger.info("{ip:%s},{url=%s},{data=%s}", request.remote_addr, request.full_path, request.json)
    # [2018 / 12 / 14 13: 57:24] [INFO][C:\Users\HM - Python\Desktop\HMdata\server - api\api\v0\payment\views.py: 111]
    # [{ip: 192.168.20.199}, {url = http: // 192.168.20.199: 5003 / bankrate_ex},
    # {data = {'bank_id': 1, 'pay_type': '1', 'fee_type': '1', 'day_max': '，', 'day_once': '1','service_charge_fee': '', 'service_charge_max': '123',service_charge_min': '12345'}}]
