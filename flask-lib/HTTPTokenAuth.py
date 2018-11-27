'''
通过请求头传Authorization: Bearer secret-token-1 与 auth 装饰器 作权限验证
'''
from flask import Flask, g
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    "secret-token-1": "John",
    "secret-token-2": "Susan"
}


@auth.verify_token
def verify_token(token):
    g.user = None
    if token in tokens:  # 验证过程
        g.user = tokens[token]  # 可以通过g传递用户
        return True
    return False


@app.route('/')
@auth.login_required  # True 才能访问
def index():
    return "Hello, %s!" % g.user


'''
HTTP头信息”Authorization: Bearer secret-token-1″，”Bearer”就是指定的scheme，”secret-token-1″就是待验证的Token。在上例中，”secret-token-1″对应着用户名”John”，所以Token验证成功
'''
