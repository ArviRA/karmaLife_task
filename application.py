from flask import Flask,jsonify,request,render_template
from flask_cors import CORS
import json
import pymongo
import pandas as pd
from pymongo import MongoClient
from IPython.display import HTML

myclient = MongoClient("mongodb+srv://MasterUser:thegoodlife@cluster0.xrlut.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["KarmaLIFE"]
collection_db = mydb["collection1"]

app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
   return render_template("index.html")


@app.route("/display",methods=["GET"])
def displayTable():
   try:
      temp_data = collection_db.find()
      print(temp_data)
      name = []
      dob = []
      gender =[]
      emp = []
      df = pd.DataFrame()
      for x in temp_data:
            name.append(x["fname"]+x["lname"])
            dob.append(x["dob"])
            gender.append(x["gender"])
            emp.append(x["employed"])
      df["Name"] = name
      df["DOB"] = dob
      df["Gender"] = gender
      df["Employed"] =emp
      #df = df.style.set_table_styles({'A': [{'selector': '','props': [('color', 'red')]}],'B': [{'selector': 'td','props': 'color: blue;'}]}, overwrite=False)
      tables= HTML(df.to_html(classes='data', header="true"))
      print(tables)

      return render_template('display.html',tables=[df.to_html(classes=None,border=0,header="true",justify="center",index=False,table_id="tablecontent")])
   except:
      pass


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