##### SQLALCHEMY
## 常用的SQLAlchemy字段类型

| 类型名       | python中类型      | 说明                                                |
| ------------ | ----------------- | --------------------------------------------------- |
| Integer      | int               | 普通整数，一般是32位                                |
| SmallInteger | int               | 取值范围小的整数，一般是16位                        |
| BigInteger   | int或long         | 不限制精度的整数                                    |
| Float        | float             | 浮点数                                              |
| Numeric      | decimal.Decimal   | 普通整数，一般是32位                                |
| String       | str               | 变长字符串                                          |
| Text         | str               | 变长字符串，对较长或不限长度的字符串做了优化        |
| Unicode      | unicode           | 变长Unicode字符串                                   |
| UnicodeText  | unicode           | 变长Unicode字符串，对较长或不限长度的字符串做了优化 |
| Boolean      | bool              | 布尔值                                              |
| Date         | datetime.date     | 时间                                                |
| Time         | datetime.datetime | 日期和时间                                          |
| LargeBinary  | str               | 二进制文件                                          |

## 常用的SQLAlchemy列选项

| 选项名      | 说明                                              |
| ----------- | ------------------------------------------------- |
| primary_key | 如果为True，代表表的主键                          |
| unique      | 如果为True，代表这列不允许出现重复的值            |
| index       | 如果为True，为这列创建索引，提高查询效率          |
| nullable    | 如果为True，允许有空值，如果为False，不允许有空值 |
| default     | 为这列定义默认值                                  |

## 常用的SQLAlchemy关系选项

| 选项名         | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| backref        | 在关系的另一模型中添加反向引用                               |
| primary join   | 明确指定两个模型之间使用的联结条件                           |
| order_by       | 指定关系中记录的排序方式                                     |
| secondary      | 指定多对多关系中关系表的名字                                 |
| secondary join | 在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件 |


~~~python
user = User()
db.session.delete(user)
user.name = "zs"
db.session.add(user)
db.session.commit()
db.create_all() # 建表
db.drop_all() # 删表


User.query.all() # 查询所有用户数据
User.query.count() # 查询有多少个用户
User.query.first() # 查询第1个用户
User.query.get(1)  # 获取id为1的数据

# 查询id为4的用户[3种方式]
    User.query.get(4)
    User.query.filter_by(id=4).all()  # 简单过滤器 接收关键字实参
    User.query.filter(User.id == 4).all()  # 复杂过滤器 接收恒等式等复杂条件

# 查询名字结尾字符为g的所有用户[开始 / 包含]
    User.query.filter(User.name.endswith("g")).all()
    User.query.filter(User.name.startswith("w")).all()
    User.query.filter(User.name.contains("w")).all()
    User.query.filter(User.name.like("%w%")).all()  # 模糊查询


# 查询名字不等于wang的所有用户[2种方式]
    from sqlalchemy import not_
    User.query.filter(not_(User.name == "wang")).all()
    User.query.filter(User.name != "wang").all()

# 查询id为[1, 3, 5, 7, 9]的用户
    User.query.filter(User.id.in_([1, 3, 5, 7, 9])).all()

# 所有用户先按年龄从小到大, 再按id从大到小排序, 取前5个
    User.query.order_by(User.age, User.id.desc()).limit(5).all()

# 分页查询, 每页3个, 查询第2页的数据
    pn = User.query.paginate(2, 3)
    pn.items 该页所有数据  pn.page 当前页码  pn.pages 总页数
~~~
##### Flask-PyMongo
~~~python
app.config.update(
    MONGO_URI='mongodb://localhost:27017/flask',
    MONGO_USERNAME='bjhee',
    MONGO_PASSWORD='111111'
)

#添加数据 insert_one() | insert_many()
    user = {'name':'Michael', 'age':18, 'scores':[{'course': 'Math', 'score': 76}]}
    mongo.db.users.insert_one(user)

#查询数据 find_one() | find()
    users = mongo.db.users.find()
    user = mongo.db.users.find_one({'name': name})

#“count()”方法, 获取返回数据集的大小
    users = mongo.db.users.find({'age':{'$lt':20}})
    print users.count()    # 打印年龄小于20的用户个数

#“sort()”方法, 排序
    # 返回所有用户，并按名字升序排序
    users = mongo.db.users.find().sort('name')
    # 返回所有用户，并按年龄降序排序
    users = mongo.db.users.find().sort('age', DESCENDING)

#“limit()”和”skip()”方法, 分页
    # 最多只返回5条记录，并且忽略开始的2条
    # 即返回第三到第七（如果存在的话）条记录
    users = mongo.db.users.find().limit(5).skip(2)

#“distinct()”方法, 获取某一字段的唯一值
    ages = mongo.db.users.find().distinct('age')
    print (ages)    # 打印 [18, 21, 17]

# 更新数据
    #“pymongo.collection.Collection”提供了两种更新数据的方法，一种是update，可以更新指定文档中某个字段的值，同关系型数据库中的update类似。update有两个函数，”update_one()”更新一条记录，”update_many()”更新多条记录：
    # 找到名为Tom的第一条记录，将其年龄加3
    result = mongo.db.users.update_one({'name': 'Tom'}, {'$inc': {'age': 3}})
    # 打印被改动过的记录数
    print('%d records modified' % result.modified_count)
    # 找到所有年龄小于20的用户记录，将其年龄设为20
    result = mongo.db.users.update_many({'age':{'$lt':20}}, {'$set': {'age': 20}})
    # 打印被改动过的记录数
    print('%d records modified' % result.modified_count)

    # 另一种更新数据的方法是replace，它不是用来更新某一字段，而是把整条记录替换掉。它就一个函数”replace_one()”：
    user = {'name': 'Lisa', 'age': 23, 'scores': [{'course': 'Politics', 'score': 95}]}
    # 找到名为Jane的第一条记录，将其替换为上面的名为Lisa的记录
    result = mongo.db.users.replace_one({'name': 'Jane'}, user)
    # 打印被改动过的记录数
    print('%d records modified' % result.modified_count)

# 删除数据
# 删除数据可以使用集合对象上的delete方法，它也有两个函数，”delete_one()”删除一条记录，”delete_many()”删除多条记录：
    # 删除名为Michael的第一条记录
    result = mongo.db.users.delete_one({'name': 'Michael'})
    # 打印被删除的记录数
    print('%d records deleted' % result.deleted_count)
    # 找到所有年龄大于20的用户记录
    result = mongo.db.users.delete_many({'age':{'$gt':20}})
    # 打印被删除的记录数
    print('%d records deleted' % result.deleted_count)
~~~