from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

a_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
a_star = a_movie['star']

db.movies.update_many({'star':a_star},{'$set':{'star':0}})