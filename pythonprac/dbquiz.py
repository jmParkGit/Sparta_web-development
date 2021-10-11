from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

matrix = db.movies.find_one({'title':'매트릭스'},{'_id':False})
matrixStar=matrix['star']
print(matrixStar)

same_stars = list(db.movies.find({'star':matrixStar},{'_id':False}))
for same_star in same_stars:
    title=same_star['title']
    print(title)

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})