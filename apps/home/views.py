from flask import render_template, session
from . import home_blue
from apps import mongo


@home_blue.route("/index")
def index():
    info1 = mongo.db.flaskdemo1.find_one()  # {'_id': ObjectId('5bf77bcd8ec0c6d1c587c2c2'), 'user': 'Astlight'}
    info2 = mongo.db.flaskdemo1.find()  # <pymongo.cursor.Cursor object at 0x0000018ECF0BBC88>
    parameter = "阿斯顿发光"
    session['user'] = '阿斯顿发光'
    return render_template("baidu.html", parameter=parameter)
