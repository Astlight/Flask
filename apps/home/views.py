from flask import render_template, session
from . import home_blue


@home_blue.route("/index")
def index():
    parameter = "阿斯顿发光"
    session['user'] = '阿斯顿发光'
    return render_template("baidu.html", parameter=parameter)
