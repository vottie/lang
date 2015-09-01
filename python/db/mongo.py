import pymongo
from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

#db = client['primer']
#coll = db['dataset']

db = client['test']
coll = db['restaurants']

result = coll.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.771903]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-02", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-10-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }

        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

# find all
#cursor = coll.find()

# find
cursor = coll.find({"borough": "Manhattan"})
for document in cursor:
    print document
