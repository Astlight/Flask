# -*- coding:utf-8 -*- 

# -*- coding:utf-8 -*-
import logging
import os
import sys
import time
from logging import handlers
from logging.handlers import RotatingFileHandler, SMTPHandler, TimedRotatingFileHandler
from instance.config import logs_path

'''
按级别分类日志器
按[debug]、[info]、[warn]、[error]及以下 四个级别分类
对存放在logs文件夹下文件名log_debug、log_info、log_warn、log_error
日志格式[2018/12/07 14:08:48] [INFO] [D:\Python36\lib\site-packages\werkzeug\_internal.py:88] [ * Running on http://0.0.0.0:5003/ (Press CTRL+C to quit)]
单个日志大小100M，最多存放10个回滚
error级别自动发送警告邮件（需配置邮箱及smtp）
Logging 下SMTPHandler本身不支持SLL，但是QQ企业邮箱需要以SSL发送SMTP, 所以重写SMTPHandler>>>CompatibleSMTPSSLHandler

'''


class CompatibleSMTPSSLHandler(handlers.SMTPHandler):
    """
    官方的SMTPHandler不支持SMTP_SSL的邮箱，这个可以两个都支持,并且支持邮件发送频率限制
    """

    def __init__(self, mailhost, fromaddr, toaddrs: tuple, subject,
                 credentials=None, secure=None, timeout=5.0, is_use_ssl=True, mail_time_interval=0):
        """

        :param mailhost:
        :param fromaddr:
        :param toaddrs:
        :param subject:
        :param credentials:
        :param secure:
        :param timeout:
        :param is_use_ssl:
        :param mail_time_interval: 发邮件的时间间隔，可以控制日志邮件的发送频率，为0不进行频率限制控制，如果为60，代表1分钟内最多发送一次邮件
        """
        super().__init__(mailhost, fromaddr, toaddrs, subject,
                         credentials, secure, timeout)
        self._is_use_ssl = is_use_ssl
        self._time_interval = mail_time_interval
        self._msg_map = dict()  # 是一个内容为键时间为值得映射

    def emit(self, record: logging.LogRecord):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        """
        from threading import Thread
        if sys.getsizeof(self._msg_map) > 10 * 1000 * 1000:
            self._msg_map.clear()
        Thread(target=self.__emit, args=(record,)).start()

    def __emit(self, record):
        if record.msg not in self._msg_map or time.time() - self._msg_map[record.msg] > self._time_interval:
            try:
                import smtplib
                from email.message import EmailMessage
                import email.utils
                t_start = time.time()
                port = self.mailport
                if not port:
                    port = smtplib.SMTP_PORT
                smtp = smtplib.SMTP_SSL(self.mailhost, port,
                                        timeout=self.timeout) if self._is_use_ssl else smtplib.SMTP(self.mailhost, port,
                                                                                                    timeout=self.timeout)
                msg = EmailMessage()
                msg['From'] = self.fromaddr
                msg['To'] = ','.join(self.toaddrs)
                msg['Subject'] = self.getSubject(record)
                msg['Date'] = email.utils.localtime()
                msg.set_content(self.format(record))
                if self.username:
                    if self.secure is not None:
                        smtp.ehlo()
                        smtp.starttls(*self.secure)
                        smtp.ehlo()
                    smtp.login(self.username, self.password)
                smtp.send_message(msg)
                smtp.quit()
                print(f'发送邮件给 {self.toaddrs} 成功，用时{round(time.time() - t_start, 2)} ,发送的内容是--> {record.msg}')
                self._msg_map[record.msg] = time.time()
            except Exception:
                self.handleError(record)
        else:
            pass
            print(f'邮件发送太频繁，此次不发送这个邮件内容： {record.msg} ')


def setup_log():
    if "logs" not in os.listdir(logs_path):
        os.mkdir(logs_path + 'logs')
        os.mkdir(logs_path + 'logs/log_info')
        os.mkdir(logs_path + 'logs/log_error')
        os.mkdir(logs_path + 'logs/log_warn')
        os.mkdir(logs_path + 'logs/log_debug')

    logs_path_info_file = (logs_path + 'logs/log_info')
    logs_path_error_file = (logs_path + 'logs/log_error')
    logs_path_warn_file = (logs_path + 'logs/log_warn')
    logs_path_debug_file = (logs_path + 'logs/log_debug')

    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    logging.basicConfig(format='[%(asctime)s] [%(levelname)s] [%(message)s]',  # [%(pathname)s:%(lineno)d]
                        datefmt='%Y/%m/%d %H:%M:%S',
                        level=logging.DEBUG)

    file_log_handler_info = TimedRotatingFileHandler(logs_path_info_file + "/log_info",
                                                     when='D',
                                                     interval=1,
                                                     backupCount=10,
                                                     encoding='utf-8')
    file_log_handler_info.suffix = "%Y-%m-%d.log"
    file_log_handler_info.setLevel(logging.INFO)

    file_log_handler_error = TimedRotatingFileHandler(logs_path_error_file + "/log_error",
                                                      when='D',
                                                      interval=1,
                                                      backupCount=10,
                                                      encoding='utf-8')
    file_log_handler_error.suffix = "%Y-%m-%d.log"
    file_log_handler_error.setLevel(logging.ERROR)

    file_log_handler_warn = TimedRotatingFileHandler(logs_path_warn_file + "/log_warn",
                                                     when='D',
                                                     interval=1,
                                                     backupCount=10,
                                                     encoding='utf-8')
    file_log_handler_warn.suffix = "%Y-%m-%d.log"
    file_log_handler_warn.setLevel(logging.WARN)

    file_log_handler_debug = TimedRotatingFileHandler(logs_path_debug_file + "/log_debug",
                                                      when='D',
                                                      interval=1,
                                                      backupCount=10,
                                                      encoding='utf-8')
    file_log_handler_debug.suffix = "%Y-%m-%d.log"
    file_log_handler_debug.setLevel(logging.DEBUG)

    # INFO,DEBUG,WARN 仅监控对应级别， ERROR向下监控所有级别
    filter_info = LogLevelFilter(level=logging.INFO)
    filter_warn = LogLevelFilter(level=logging.WARN)
    filter_debug = LogLevelFilter(level=logging.DEBUG)

    file_log_handler_info.addFilter(filter_info)
    file_log_handler_warn.addFilter(filter_warn)
    file_log_handler_debug.addFilter(filter_debug)

    formatter_info = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(message)s]',
                                       datefmt='%Y/%m/%d %H:%M:%S') # 不含[%(pathname)s:%(lineno)d]
    file_log_handler_info.setFormatter(formatter_info)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(pathname)s:%(lineno)d] [%(message)s]',
                                  datefmt='%Y/%m/%d %H:%M:%S')
    file_log_handler_error.setFormatter(formatter)
    file_log_handler_warn.setFormatter(formatter)
    file_log_handler_debug.setFormatter(formatter)

    # 日志error邮件 smtp.exmail.qq.com(使用SSL，端口号465)
    # mail_handler = CompatibleSMTPSSLHandler(log_mailhost, log_fromaddr, log_toaddrs,log_subject, log_credentials)
    # mail_handler.setLevel(logging.ERROR)
    # logger.addHandler(mail_handler)

    logger.addHandler(file_log_handler_info)
    logger.addHandler(file_log_handler_warn)
    logger.addHandler(file_log_handler_error)
    logger.addHandler(file_log_handler_debug)
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
    pass
    # print(logs_path)
    # print(os.listdir(logs_path))
    # logger = setup_log()
    # logger.debug('for debug')
    # logger.info('for debug')
    # logger.error('for error')
    # logger.fatal('for FATAL')
