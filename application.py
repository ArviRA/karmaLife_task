from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/")
def insertVal():
   print("came inside")
   return jsonify({"data":200})

if __name__ == '__main__':
   app.run()