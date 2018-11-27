import jwt

from config import Config

encoded_jwt = jwt.encode({'parameter': '阿斯顿发光'}, Config.SECRET_KEY, algorithm='HS256')
print(encoded_jwt)
print(jwt.decode(encoded_jwt, Config.SECRET_KEY, algorithms=['HS256']))
