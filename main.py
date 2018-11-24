from flask import request, make_response, Response, jsonify, render_template, send_file
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_wtf.csrf import generate_csrf
from apps import create_app
from forms import addUserForm

app = create_app("dev")
mgr = Manager(app)  # flask_script 管理
mgr.add_command("mg", MigrateCommand)  # flask_script 管理
# $ python main.py mg init 初始化生成文件夹
# $ python main.py mg migrate -m "备注" . 生成表迁移版本py文件
# $ python main.py mg upgrade .同步表结构至数据库
# 降级有bug， 只升不降。

@app.route('/', methods=["GET", "POST"])
def hello_world():
    '''请求与响应'''

    '''接收参数'''
    print(request.args.get("name"))  # Method=GET,URL传参
    print(request.form.get("name"))  # Method=POST,表单传参
    print(request.data.decode())  # Json bytes类型

    file = request.files.get("name")  # Method=POST,表单传文件 > FileStorage
    if file:
        print(file.content_type)  # >>> image/jpeg
        file.save("目录.jpg")

    '''set_session,flask自动根据secret_key生成session.id（默认存在服务器内存中）'''
    # session["uid"] = uid
    # session["username"] = username

    '''get_session'''
    # uid = session.get("uid")
    # if uid:
    #     return "user_information"

    '''异常'''
    # abort(403)  # >>> rasie 异常

    '''响应'''
    response = make_response("index")  # type: Response
    return response, 700  # 返回响应对象 + 状态码
    # return 'index' # 返回字符串/bytes
    # return jsonify(dict)  # content-type = application/json
    # return redirect('http://www.baidu.com')  # 重定向至url
    # return redirect(url_for("index")  # 重定向至视图函数


@app.errorhandler(404)
def not_found_handler(e):
    '''404统一处理'''
    return "url_for 404 or static 404 html.%s" % e


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        csrf_token = generate_csrf()  # 前后端分离生成token
        response = make_response(send_file("templates/login.html"))
        response.set_cookie("csrf_token", csrf_token)  # == (request.headers["X-Csrftoken"])
        # 前端 headers:{"X-CSRFToken":getCookie("csrf_token")}
        return response
        # return render_template('login.html', form=addUserForm())  # 来返回send_file静态html，这个html不经过jinja2修饰。render_template返回后端渲染html,经过jinja2修饰

    elif request.method == "POST":
        form = addUserForm()
        if form.validate_on_submit():
            return jsonify({
                "status": "success",
                "msg": "添加成功",
                "data": {
                    "name": form.username.data,
                    "password": form.password.data
                }
            })
            # 验证未通过
        return jsonify({
            "status": "failed",
            "msg": "添加失败",
            "error": form.errors
        })


@app.route("/templates")
def templates():
    parameter = "阿斯顿发光"
    return render_template("baidu.html", parameter=parameter)  # 模板渲染 {{ parameter | 过滤器 }} （ 支持对象属性，对象方法，函数）


# view-flash("message"),T-{{get_flashed_message()}} 遍历取出message
# render默认会对参数的符号标记进行转义，通过过滤器safe取消转义。
'''
{% for data in my_list if data.id != 5 %} {# loop只能在循环内部使用 #}     
    {% if loop.index == 1 %}       index start from 1, index0 startf from 0  
        <li style="background-color: #ffb300">{{ data.value }}</li>     
    {% elif loop.index == 2 %}         
        <li style="background-color: #ff0000">{{ data.value }}</li>     
    {% else %}         
        <li style="background-color: #1cb7fd">{{ data.value }}</li>     
    {% endif %} 
{% endfor %}
'''


@app.route("/url_parameter/<parameter>")  # /url_parameter/1
# @app.route("/url_parameter/<int:parameter>||<string(length=2):parameter>")
# 正则parameter|BaseConverter(werkzeug) 可自定义
# 底层to_python方法，在传给视图之前触发，可以对路由变量进行加工。（大小写敏感，str转int）
def url_parameter(parameter):
    return parameter


if __name__ == "__main__":
    # print(app.url_map)  # >>> Map([<Rule '/' (OPTIONS, HEAD, GET) -> hello_world>
    #  <Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static>])
    # app.run(host="0.0.0.0", port=5000, debug=True,load_dotenv=True)
    mgr.run()  # flask_script脚本管理 $ python main.py runserver -h 0.0.0.0 -p 5000
