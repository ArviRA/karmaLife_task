import pymongo
from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://MasterUser:thegoodlife@cluster0.xrlut.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["KarmaLIFE"]
collection_db = mydb["collection1"]


def update_db(data_dict):
    collection_db.insert_one(data_dict)
    return