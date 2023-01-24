import pymongo
from pymongo import MongoClient
from index import *

client = MongoClient()
db = client.aguaViva
collection = db.waterInfo

data = {
    "liters":{qtLiters},
    "mCubic":{mCubic},
    "price":{price},
}

collection.insert_one(data)