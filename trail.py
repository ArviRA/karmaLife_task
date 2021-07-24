import pymongo
from pymongo import MongoClient
myclient = MongoClient("mongodb+srv://MasterUser:thegoodlife@cluster0.xrlut.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["KarmaLIFE"]
temp = mydb["collection1"]

post = {'id':1,'fname':'Shaki','lname':'C'}

temp.insert_one(post)
 


 