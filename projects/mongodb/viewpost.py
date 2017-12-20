import pymongo
from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client.mongo_testdb



posts = db.posts
result = posts.find_one({'author': 'Scott'})
print(result)

