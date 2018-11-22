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
    # user = User()
    # db.session.delete(user)
    # user.name = "zs"
    # db.session.add(user)
    # db.session.commit()
    # db.create_all() # 建表
    # db.drop_all() # 删表
"""
    查询所有用户数据
    User.query.all()
    查询有多少个用户
    User.query.count()
    查询第1个用户
    User.query.first()
    User.query.get(1)  # 获取id为1的数据
    查询id为4的用户[3种方式]
    User.query.get(4)
    User.query.filter_by(id=4).all()  # 简单过滤器 接收关键字实参
    User.query.filter(User.id == 4).all()  # 复杂过滤器 接收恒等式等复杂条件
    查询名字结尾字符为g的所有用户[开始 / 包含]
    User.query.filter(User.name.endswith("g")).all()
    User.query.filter(User.name.startswith("w")).all()
    User.query.filter(User.name.contains("w")).all()
    User.query.filter(User.name.like("%w%")).all()  # 模糊查询
    查询名字和邮箱都以li开头的所有用户[2种方式]
    User.query.filter(User.name.startswith("li"), User.email.startswith("li")).all()
    from sqlalchemy import and_
    User.query.filter(and_(User.name.startswith("li"), User.email.startswith("li"))).all()
    查询age是25 或者 `email`以`itheima.com`结尾的所有用户
    from sqlalchemy import or_
    User.query.filter(or_(User.age == 25, User.email.endswith("itheima.com"))).all()
    查询名字不等于wang的所有用户[2种方式]
    from sqlalchemy import not_
    User.query.filter(not_(User.name == "wang")).all()
    User.query.filter(User.name != "wang").all()
    查询id为[1, 3, 5, 7, 9]的用户
    User.query.filter(User.id.in_([1, 3, 5, 7, 9])).all()
    所有用户先按年龄从小到大, 再按id从大到小排序, 取前5个
    User.query.order_by(User.age, User.id.desc()).limit(5).all()
    分页查询, 每页3个, 查询第2页的数据
    pn = User.query.paginate(2, 3)
    pn.items 该页所有数据  pn.page 当前页码  pn.pages 总页数
    """
