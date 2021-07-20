import pandas as pd
import pymongo
from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://MasterUser:thegoodlife@cluster0.xrlut.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["KarmaLIFE"]
collection_db = mydb["collection1"]

def get_data():
    temp_data = collection_db.find()
    print(temp_data)
    name = []
    dob = []
    gender =[]
    emp = []
    df = pd.DataFrame()
    for x in temp_data:
        name.append(x["fname"]+" "+x["lname"])
        dob.append(x["dob"])
        gender.append(x["gender"])
        emp.append(x["employed"])
    df["Name"] = name
    df["DOB"] = dob
    df["Gender"] = gender
    df["Employed"] =emp
    return df