# -*- coding:utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler


def setup_log():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_log_handler_info = RotatingFileHandler("logs/log_info", maxBytes=1024 * 1024 * 100, backupCount=10)
    file_log_handler_info.setLevel(logging.INFO)

    file_log_handler_debug = RotatingFileHandler("logs/log_debug", maxBytes=1024 * 1024 * 100, backupCount=10)
    file_log_handler_debug.setLevel(logging.DEBUG)

    file_log_handler_error = RotatingFileHandler("logs/log_error", maxBytes=1024 * 1024 * 100, backupCount=10)
    file_log_handler_error.setLevel(logging.ERROR)

    file_log_handler_warn = RotatingFileHandler("logs/log_warn", maxBytes=1024 * 1024 * 100, backupCount=10)
    file_log_handler_warn.setLevel(logging.WARN)

    # INFO,DEBUG,WARN 仅监控对应级别， ERROR向下监控所有级别
    filter_info = LogLevelFilter(level=logging.INFO)
    filter_debug = LogLevelFilter(level=logging.DEBUG)
    filter_warn = LogLevelFilter(level=logging.WARN)

    file_log_handler_info.addFilter(filter_info)
    file_log_handler_debug.addFilter(filter_debug)
    file_log_handler_warn.addFilter(filter_warn)

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(message)s',
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
# -*- coding:utf-8 -*-

