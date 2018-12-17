from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.before_first_request
def initial():
    print("第一次请求服务器的url时会调用, 主要完成一些初始化操作, 如连接数据库")


@app.before_request
def prepare():
    print("每次请求前会调用, 主要完成一些准备工作, 如参数校验, 数据统计, 过滤黑名单")


@app.after_request
def process(response):  # 一旦设置该装饰器, 参数必须接收响应对象, 并且返回一个响应对象
    print("每次请求后会调用, 主要完成一些对响应的加工处理, 如设置统一的响应头信息, 包装数据")
    return response


@app.teardown_request
def err_handle(error):  # 一旦设置该装饰器, 参数必须接收错误信息对象, 但是如果没有出现异常, error为None
    print("每次请求后调用, 无论是否出现异常, 主要完成请求的最后处理, 如记录异常信息 %s" % error)


@app.before_request
def logger_setup():
    if request.method == 'GET':
        logger.info("========请求信息========:[ip=%s],[method=%s],[url=%s],[request_data=%s]", request.remote_addr, request.method, request.full_path, dict(request.args))
    if request.method == 'POST':
        if request.json == {}:
            logger.info("========请求信息========:[ip=%s],[method=%s],[url=%s],[request_data=%s]", request.remote_addr, request.method,request.full_path, request.json)
        elif request.json is None:
            logger.info("========请求信息========:[ip=%s],[method=%s],[url=%s],[request_data=%s]", request.remote_addr, request.method,request.full_path, request.json)
            return jsonify(code_no=RET.METHODERR, code_msg=error_map[RET.METHODERR])
    return

@app.after_request
def process(response):
    logger.info("========响应信息========:[ip=%s],[method=%s],[url=%s],[response_data=%s]", request.remote_addr, request.method,request.full_path, response.data.decode())
    return response


if __name__ == '__main__':
    app.run(debug=True)
