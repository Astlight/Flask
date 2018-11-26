from flask import render_template, session, current_app, request
from flask_login import login_required

from config import Config
from . import home_blue
from apps import mongo, limiter, cache, login_manager


@home_blue.route("/index")
@cache.cached(timeout=60 * 2)
# @login_required
def index():
    try:
        print(mongo.db.flaskdemo1.find_one())  # {'_id': ObjectId('5bf77bcd8ec0c6d1c587c2c2'), 'user': 'Astlight'}
        print(mongo.db.flaskdemo1.find())  # <pymongo.cursor.Cursor object at 0x0000018ECF0BBC88>
    except BaseException as e:
        current_app.logger.error("错误记录至日志及控制台: %s" % e)
    session['user'] = '阿斯顿发光'
    parameter = "阿斯顿发光"
    import jwt
    encoded_jwt = jwt.encode({'parameter': parameter}, Config.SECRET_KEY, algorithm='HS256')
    print(encoded_jwt)
    print(jwt.decode(encoded_jwt, Config.SECRET_KEY, algorithms=['HS256']))

    return render_template("baidu.html", parameter=parameter)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
