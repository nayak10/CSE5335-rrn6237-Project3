# -*- coding: utf-8 -*-
"""

Created on Tue Oct 06 14:13:33 2015

@author: Rajesh Nayak
"""

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! Welcome."
    
@app.route("/user/<username>")
def xxxxxx(username):
    return render_template('final.html', name=username)
    
@app.route("/lotsofdata", methods=["GET", "POST"])
def people():
    #ind = request.form.get('ind')
    #print ("ind =   " , ind)
    mongolab_uri = "mongodb://heroku_9crjjz3b:eo0hbm9sgq5lkre3503kr3prsr@ds055584.mongolab.com:55584/heroku_9crjjz3b"
    para = {}
    
    client = MongoClient(mongolab_uri,connectTimeoutMS=30000,socketTimeoutMS=None,socketKeepAlive=True)
    db = client.get_default_database()
    cursor = db.footballers.find()
    #print(type(cursor))
    for document in cursor:
        
        para[str(document['PlayerID'])] = str(document['PlayerName'])
        
        #print para
    #return render_template("index.html", PID = str(document['PlayerID']), PNAME = str(document['PlayerName']), TNAME = str(document['TeamName']) )
    return jsonify(**para)
    
if __name__ == "__main__":
    app.run(debug=True)
    
    app.run(host = "127.0.0.1", port = 5000)
    