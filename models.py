from main import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    addresses = db.relationship("Address", backref="user_attr")
    # print(user.addresses)  db.relationship("类名", backref="取值时的属性名add.user")


class Address(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(32), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # add = Address(detail="Asdfg",user_id=user.id)

# 多对多需单独建关系表,Lazy="dynamic" 优化性能

if __name__ == '__main__':
    pass
