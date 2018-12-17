from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from apps import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    money = db.Column(db.Numeric(10, 2), default=0.00, nullable=False)  # 账号金额
    avatar_url = db.Column(db.String(256))  # 用户头像路径
    last_login = db.Column(db.DateTime, default=datetime.now)  # 最后一次登录时间 last_login.strftime("%Y-%m-%d %H:%M:%S")
    is_admin = db.Column(db.Boolean, default=False)
    signature = db.Column(db.String(512))  # 用户签名
    gender = db.Column(  # 订单的状态
        db.Enum(
            "MAN",  # 男
            "WOMAN"  # 女
        ),
        default="MAN")
    addresses = db.relationship("Address", backref="user_attr")

    # print(user.addresses)  db.relationship("类名", backref="取值时的属性名add.user")



    # def __init__(self, user_id=None, account_number=None, password=None, name="anonymous"):
    #     self.user_id = user_id
    #     self.accountNumber = account_number
    #     self.password = password
    #     self.name = name
    #
    # def is_authenticated(self):
    #     return True
    #
    # def is_active(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return False
    #
    # def get_id(self):
    #     return self.user_id  # unicode
    #
    # def __repr__(self):
    #     return '<User %r>' % (self.accountNumber)

    @property
    def password(self):
        raise AttributeError("该属性是计算性属性, 不能直接取值")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):  # 封装密码校验过程
        return check_password_hash(self.password_hash, password)


class Address(BaseModel, db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(32), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # add = Address(detail="Asdfg",user_id=user.id)
    # 多对多需单独建关系表,Lazy="dynamic" 优化性能

class T_Bank(db.Model):
    '''
    银行表
    '''
    __tablename__ = "t_bank"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, comment="流水号")
    name = db.Column(db.String(20), unique=True)  # 银行名
    status = db.Column(db.Enum("0", "1"), server_default="0", nullable=False, comment="0:正常，1:冻结")  # 状态位
    del_flg = db.Column(db.Enum("0", "9"), server_default="0", nullable=False, comment="0:有效, 9:删除")  # 删除标志位
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)  # 创建时间
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)  # 更新时间
    create_account_id = db.Column(db.Integer)  # 创建人id
    update_account_id = db.Column(db.Integer)  # 更新人id


class T_Ex_Quota(db.Model):
    '''
    对外限额表
    '''
    __tablename__ = "t_ex_quota"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, comment="流水号")
    bank_id = db.Column(db.Integer, nullable=False, comment="t_bank.id")
    pay_type = db.Column(db.Enum("1", "2", "3"), nullable=False, server_default="1",
                         comment="1:协议代扣, 2:协议支付, 3:大额支付")  # 支付类型
    day_max = db.Column(db.Numeric(12, 2), comment="空 没有限制")  # 单日限额
    day_once = db.Column(db.Numeric(12, 2), comment="空 没有限制")  # 单次限额
    service_charge_max = db.Column(db.Numeric(12, 2), comment="空 没有限制")  # 上限限额
    service_charge_min = db.Column(db.Numeric(12, 2), comment="空 没有限制")  # 下限限额
    fee_type = db.Column(db.Enum("1", "2", "3"), server_default="1", nullable=False,
                         comment="1:百分比, 2:固定金额, 3:特殊规则")  # 手续费类型
    service_charge_fee = db.Column(db.Numeric(5, 2), server_default='0.00',
                                   comment="rate_type=1时,放费率*100后的值rate_type=2时,放固定金额")  # 手续费
    status = db.Column(db.Enum("0", "1"), server_default="0", nullable=False, comment="0:正常，1:冻结")  # 状态位
    del_flg = db.Column(db.Enum("0", "9"), server_default="0", nullable=False, comment="0:有效， 9:删除")  # 删除标志位
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)  # 创建时间
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)  # 更新时间
    create_account_id = db.Column(db.Integer)  # 创建人id
    update_account_id = db.Column(db.Integer)  # 更新人id


if __name__ == '__main__':
    pass
