import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_pymongo import PyMongo
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import config_dict

# 数据库初始化全局
db = None  # type: SQLAlchemy
sr = None  # type: StrictRedis
mongo = None  # type: PyMongo


# 配置日志文件(将日志信息写入到文件中)
def setup_log():
    # 设置日志的记录等级
    logging.basicConfig(level=logging.DEBUG)  # 调试debug级与以下都显示 # ERROR
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(pathname)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_type):
    config_class = config_dict[config_type]
    app = Flask(__name__,
                static_url_path=None,  # 静态文件的访问路径，可改/test/login.html >>> 实际访问static/login.html
                static_folder='static',
                static_host=None,
                host_matching=False,
                subdomain_matching=False,
                template_folder='templates',
                instance_path=None,
                instance_relative_config=False,
                root_path=None)
    app.config.from_object(config_class)  # 加载配置

    Session(app)  # 管理session
    global db, sr, mongo
    db = SQLAlchemy(app)  # 管理Mysql
    sr = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)  # 管理redis
    mongo = PyMongo(app)  # 管理mongo
    Migrate(app, db)  # 数据库迁移
    CORS(app, supports_credentials=True)  # 开启CORS跨域
    CSRFProtect(app)  # 对所有Post请求进行CSRF验证，从cookie和请求头中取出csrf_token, 如果失败返回拒绝访问. 必开
    # 注册蓝图
    from apps.home import home_blue
    app.register_blueprint(home_blue)

    # 配置日志文件
    setup_log()

    return app
