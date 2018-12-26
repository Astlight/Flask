import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
# from flask_cache import Cache
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import config_dict, redis_cache_config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# 数据库初始化全局
db = None  # type: SQLAlchemy
sr = None  # type: StrictRedis
mongo = None  # type: PyMongo
limiter = None  # type: Limiter
# cache = None  # type: Cache
login_manager = None  # type: LoginManager
api = None  # type:Api


# 配置日志文件(将日志信息写入到文件中)
def setup_log(LOGLEVEL):
    # 设置日志的记录等级
    logging.basicConfig(level=LOGLEVEL)  # 调试debug级 与以下都显示 # ERROR
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
    app = Flask(__name__,  # __name__ 定义static和templates位置
                static_url_path=None,  # 静态文件的访问路径，可改/test/login.html >>> 实际访问static/login.html
                static_folder='../static',
                static_host=None,
                host_matching=False,
                subdomain_matching=False,
                template_folder='../templates',
                instance_path=None,
                instance_relative_config=False,
                root_path=None)
    app.config.from_object(config_class)  # 加载配置
    Session(app)  # 管理session
    global db, sr, mongo, limiter, cache, login_manager, api
    # auth = Auth()
    # jwt = JWT(app, auth.authenticate, auth.identity)
    # login_manager = LoginManager(app)
    # login_manager.login_view = "user.login"  # 被拦截后统一跳到user/login这个路由下
    api = Api(app)  # restful / Resource/ api.add_resource(TodoSimple, '/<string:todo_id>')

    # cache = Cache(app, config=redis_cache_config)  # redis缓存
    limiter = Limiter(app=app, key_func=get_remote_address, default_limits=[
        "1000/day, 60/minute, 5/second"])  # 限流,default_limits对所有视图有效 | # @limiter.exempt  取消默认限制器 | @limiter.limit("100/day;10/hour;3/minute") 自定义视图限制器

    db = SQLAlchemy(app)  # 管理Mysql
    sr = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, db=config_class.REDIS_DB,
                     decode_responses=True)  # 管理redis
    mongo = PyMongo(app)  # 管理mongo
    Migrate(app, db)  # 数据库迁移
    CORS(app, supports_credentials=True)  # 开启CORS跨域
    # CSRFProtect(app)  # 对所有Post请求进行CSRF验证，从cookie和请求头中取出csrf_token, 如果失败返回拒绝访问. 必开
    # 注册蓝图
    from apps.home import home_blue

    app.register_blueprint(home_blue)
    from apps.register import register_blue
    app.register_blueprint(register_blue)

    # 配置日志文件
    setup_log(config_class.LOGLEVEL)

    # 为数据迁移导入models文件
    import models

    return app
