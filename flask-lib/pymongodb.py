# -*- coding:utf-8 -*- 

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]  # 创建的数据库databases runoobdb
# dblist = myclient.list_database_names() # >>> databases_list
mycol = mydb["sites"]  # 创建集合tables sites
# collist = mydb. list_collection_names() # >>> tables_list

# !!! Python Mongodb 插入文档 !!!
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = mycol.insert_one(mydict)
print(x)  # <pymongo.results.InsertOneResult object at 0x00000131525951C8>
print(x.inserted_id)  # 5c23552f0e22113c642483a9

mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]
x = mycol.insert_many(mylist)
# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)  # [ObjectId('5c23552f0e22113c642483aa'),]

# !!! Python Mongodb 查询文档 !!!
x = mycol.find_one()  # one
for x in mycol.find():  # all
    print(x)

'''
find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。
除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
'''
# for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1 }):
# for x in mycol.find({},{ "alexa": 0 }):

# 根据指定条件查询
myquery = {"name": "RUNOOB"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# 高级查询,
myquery = {"name": {"$gt": "H"}}
# 使用正则表达式查询,
# 返回指定条数记录
myresult = mycol.find().limit(3)

# !!! Python Mongodb 修改文档 !!!
myquery = {"alexa": "10000"}
newvalues = {"$set": {"alexa": "12345"}}
mycol.update_one(myquery, newvalues)
myquery = {"name": {"$regex": "^F"}}
mycol.update_many(myquery, newvalues)

# !!! Python Mongodb 删除数据 !!!
myquery = {"name": "Taobao"}
mycol.delete_one(myquery)
myquery = {"name": {"$regex": "^F"}}
mycol.delete_many(myquery)

mycol.delete_many({})  # 删除集合中所有文档
mycol.drop()  # 删除集合

# !!! 排序 !!!
mydoc = mycol.find().sort("alexa")  # 升
mydoc = mycol.find().sort("alexa", -1)  # 降

'''
嵌入式关系
{
   "_id":ObjectId("52ffc33cd85242f436000001"),
   "contact": "987654321",
   "dob": "01-01-1991",
   "name": "Tom Benzamin",
   "address": [
      {
         "building": "22 A, Indiana Apt",
         "pincode": 123456,
         "city": "Los Angeles",
         "state": "California"
      },
      {
         "building": "170 A, Acropolis Apt",
         "pincode": 456789,
         "city": "Chicago",
         "state": "Illinois"
      }]
} 
引用式关系
{
   "_id":ObjectId("52ffc33cd85242f436000001"),
   "contact": "987654321",
   "dob": "01-01-1991",
   "name": "Tom Benzamin",
   "address_ids": [
      ObjectId("52ffc4a5d85242602e000000"),
      ObjectId("52ffc4a5d85242602e000001")
   ]
}
'''
