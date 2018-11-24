from flask import render_template, session, current_app
from . import home_blue
from apps import mongo


@home_blue.route("/index")
def index():
    try:
        print(mongo.db.flaskdemo1.find_one())  # {'_id': ObjectId('5bf77bcd8ec0c6d1c587c2c2'), 'user': 'Astlight'}
        print(mongo.db.flaskdemo1.find())  # <pymongo.cursor.Cursor object at 0x0000018ECF0BBC88>
    except BaseException as e:
        current_app.logger.error("错误记录至日志及控制台: %s" % e)

    session['user'] = '阿斯顿发光'
    parameter = "阿斯顿发光"
    return render_template("baidu.html", parameter=parameter)
