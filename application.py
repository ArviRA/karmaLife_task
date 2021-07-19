from flask import Flask,jsonify,request,render_template
from flask_cors import CORS
import json
import pymongo
from pymongo import MongoClient
myclient = MongoClient("mongodb+srv://MasterUser:thegoodlife@cluster0.xrlut.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["KarmaLIFE"]
collection_db = mydb["collection1"]

app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
   return render_template("index.html")


@app.route("/insertDATA",methods=["GET","POST"])
def insertVal():
   try:
      data_dict = request.data
      data_dict =  json.loads(data_dict.decode())

      print(data_dict)
      collection_db.insert_one(data_dict)
      return jsonify({"status":200})
   except:
      return jsonify({"status":500})


if __name__ == '__main__':
   app.run(debug=True)