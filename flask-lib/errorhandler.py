from flask import current_app


@current_app.errorhandler(404)
def not_found_handler(e):
    '''404统一处理'''
    return "url_for 404 or static 404 html. %s" % e


@current_app.errorhandler(429)  # 限流捕获
def not_found_handler(e):
    '''404统一处理'''
    return "flask-limiter. %s" % e
