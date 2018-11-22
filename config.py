from datetime import timedelta

from redis import StrictRedis


class Config:
    SECRET_KEY = "A13Nodi8EK7tlsKoaJlnwD/1VYxmC6vVk74t16s6ohrxl6kPbSNGGaN1GBYeeyEv"  # base64.b64encode(os.urandom(48))
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False  # 返回json可显示中文
    REDIS_PORT = 6379
    REDIS_HOST = "127.0.0.1"
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = False  # 对Session加密
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
