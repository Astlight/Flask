import time

from models import User


class Auth():
    def error_handler(self, e):
        print(e)
        return "Something bad happened", 400

    def authenticate(self, username, password):
        userInfo = User.query.filter_by(username=username).first()
        if (userInfo is None):
            self.error_handler('找不到用户')
        else:
            if (User.check_password(User, userInfo.password, password)):
                login_time = int(time.time())
                userInfo.login_time = login_time
                User.update(User)
                return userInfo
            else:
                self.error_handler('密码不正确')

    def identity(self, payload):
        id = payload['identity']
        return Users.get(Users, id)
