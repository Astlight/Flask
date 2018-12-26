import logging
from datetime import timedelta

from redis import StrictRedis


class Config:
    SECRET_KEY = "A13Nodi8EK7tlsKoaJlnwD/1VYxmC6vVk74t16s6ohrxl6kPbSNGGaN1GBYeeyEv"  # base64.b64encode(os.urandom(48))
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:mysql@127.0.0.1:3306/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False  # 返回json可显示中文
    SESSION_TYPE = 'redis'
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 0  # 普通redis存在0
    SESSION_REDIS_DB = 3  # SESSION 存在redis db3
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=SESSION_REDIS_DB)
    SESSION_USE_SIGNER = True  # 对Session加密
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    MONGO_DBNAME = 'flask'
    MONGO_URI = 'mongodb://127.0.0.1:27017/flask'


class DevelopConfig(Config):
    DEBUG = True
    LOGLEVEL = logging.DEBUG


class ProductConfig(Config):
    DEBUG = True
    LOGLEVEL = logging.ERROR


config_dict = {
    "dev": DevelopConfig,
    "pro": ProductConfig
}

redis_cache_config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': '1',
    'CACHE_REDIS_PASSWORD': ''
}
