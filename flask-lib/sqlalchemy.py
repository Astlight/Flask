# -*- coding:utf-8 -*- 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://mysql:mysql@127.0.0.1:3306/flask_DB")

Session = sessionmaker(bind=engine)

Base = declarative_base()


class Users(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "Students"
    Sno = Column(String(10), primary_key=True)  # Column类创建一个字段
    Sname = Column(String(20), nullable=False, unique=True, index=True)
    Ssex = Column(String(2), nullable=False)
    Sage = Column(Integer, nullable=False)
    Sdept = Column(String(20))


# 创建session对象:
session = Session()
# 创建新User对象:
new_user = Users(Sno='5', Sname='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
ret = session.query(Users).all()
ret = session.query(Users.id, Users.extra).all()  # 结果为一个列表
ret = session.query(Users).filter_by(name='cc').first()
ret = session.query(Users).filter_by(name='cc').all()

session.query(Users).filter(Users.id> 2).update({"name": "099"})
session.query(Users).filter(Users.id > 2).update({Users.name: Users.name + "099"}, synchronize_session=False)
session.query(Users).filter(Users.id > 2).update({"num": Users.num + 1}, synchronize_session="evaluate")
session.commit()
