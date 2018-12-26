# -*- coding:utf-8 -*- 

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

message = 'hello ghost, this is a plian text'
with open('ghost-public.pem',"r") as f:
     key = f.read()
     rsakey = RSA.importKey(key)  # 导入读取到的公钥
     cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
     cipher_text = base64.b64encode(cipher.encrypt(message.encode(encoding="utf-8")))  # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
     print(cipher_text)

with open('ghost-private.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)  # 导入读取到的私钥
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    text = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    print(text)
# 结果：
b'meBtYXP35VNjtWXsONDluweXdG98tMHjb5GxBLFJ0GJzo+96wSrHe8SDhNJweDJP6/OdeIQ8jP1HKCK+aC9HA12YMSUUqcixsY5s8QUyTs+fkMjGrlC6I7hPLO4DGQbFXEY0jiqP9ycgmAi5FCsDMcm0oEm8/fVzv7vl9QarSN4='  # 加密后的密文
b'hello ghost, this is a plian text'  # 解密后的明文