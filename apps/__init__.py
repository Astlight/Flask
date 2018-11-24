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
    return app
