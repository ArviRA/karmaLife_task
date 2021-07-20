from flask import Flask,jsonify,request,render_template,render_template_string
from flask_cors import CORS
import json
import pymongo
import pandas as pd
from pymongo import MongoClient
from IPython.display import HTML
from viewEmployees import get_data
from insertEmployees import update_db


app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
   return render_template("insertEmployees.html")


@app.route("/viewEmployees",methods=["GET"])
def displayTable():
   try:
      df = get_data()
      return render_template('viewEmployees.html',tables=[df.to_html(classes=None,border=0,header="true",justify="center",index=False,table_id="tablecontent")])
   except:
      return render_template_string('''<!doctype html><html><head></head><body><p>Something Went Wrong Try Again</p></body></html>''')


@app.route("/insertEmployees",methods=["GET","POST"])
def insertVal():
   try:
      data_dict = request.data
      data_dict =  json.loads(data_dict.decode())
      update_db(data_dict)
      return jsonify({"status":200})
   except:
      return jsonify({"status":500})


if __name__ == '__main__':
   app.run(debug=True)