from pymongo import MongoClient

url = 'mongodb+srv://admin:admin@cluster0.gksk1qf.mongodb.net'

client = MongoClient(url)
db = client.pytech

header =  '-- Pytech Collection List --'
print (header)

print(db.list_collection_names())