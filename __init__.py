from flask import Flask, Response, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'textq-a'
app.config['MONGO_URI'] = 'mongodb://user1:green1@ds163402.mlab.com:63402/textq-a'

mongo = PyMongo(app)

@app.route('/display')
def display():
    #nodes = mongo.db.collection.find()
    #json_nodes = []
    #for node in nodes:
    #    json_nodes.append(node)
    #json_nodes = json.dumps(json_nodes, default = json_util.default)
    #return json_nodes

    connection = MongoClient('mongodb://user1:green1@ds163402.mlab.com:63402/textq-a')
    collection = connection['textq-a']['text-input']
    nodes = collection.find()
    #l =  list(nodes)
    #json_nodes = json.dumps(nodes, default = json_util.default)
    #return json_nodes
    json_nodes = []
    for node in nodes:
        json_nodes.append(node)
    json_nodes = json.dumps(json_nodes, default = json_util.default)
    return json_nodes

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template("page1.html")



@app.route('/ml.html', methods = ['GET', 'POST'])
def machine_learning():
    return render_template("ml.html")

@app.route('/nlp.html', methods = ['GET', 'POST'])
def nlp():
    return render_template("nlp.html")

@app.route('/cv.html', methods = ['GET', 'POST'])
def cv():
    return render_template("cv.html")

@app.route('/speech.html', methods = ['GET', 'POST'])
def speech():
    return render_template("speech.html")


@app.route('/img_domain.html', methods = ['GET', 'POST'])
def domain():
    return render_template("img_domain.html")


@app.route('/img_rec_tree.html', methods = ['GET', 'POST'])
def visual_example():
    return render_template("img_rec_tree.html")

@app.route('/text_CI.html', methods = ['GET', 'POST'])
def text_CI():
    return render_template("text_CI.html")

@app.route('/textI.html', methods = ['GET', 'POST'])
def text_input():
    connection = MongoClient('mongodb://user1:green1@ds163402.mlab.com:63402/textq-a')
    collection = connection['textq-a']['text-input']
    nodes = collection.find({}, {'_id': False})
    #l = list(nodes)
    #json_nodes = json.dumps(l, default=json_util.default)
    #return json_nodes
    json_nodes = []
    for node in nodes:
        json_nodes.append(node)
    json_nodes = json.dumps(json_nodes, default=json_util.default)
    return render_template("textI.html", data = json_nodes)

@app.route('/data')
def data():
    connection = MongoClient('mongodb://user1:green1@ds163402.mlab.com:63402/textq-a')
    collection = connection['textq-a']['text-input']
    nodes = collection.find({}, {'_id': False})
    # l = list(nodes)
    # json_nodes = json.dumps(l, default=json_util.default)
    # return json_nodes
    json_nodes = []
    for node in nodes:
        json_nodes.append(node)
    json_nodes = json.dumps(json_nodes, default=json_util.default)
    connection.close()
    return json_nodes

@app.route('/update')
def update():
    connection = MongoClient('mongodb://user1:green1@ds163402.mlab.com:63402/textq-a')
    collection = connection['textq-a']['text-input']

    myquery = {"name": "Son of A"}
    newvalues = {"$set": {"name": "SA"}}

    collection.update_one(myquery, newvalues)

    return 'Records updated succesfully'


@app.route('/text_context.html', methods = ['GET', 'POST'])
def text_context():
    return render_template("text_context.html")

@app.route('/voice_CI.html', methods = ['GET', 'POST'])
def voice_CI():
    return render_template("voice_CI.html")

@app.route('/voice_input.html', methods = ['GET', 'POST'])
def voice_input():
    return render_template("voice_input.html")

@app.route('/voice_context.html', methods = ['GET', 'POST'])
def voice_context():
    return render_template("voice_context.html")


if __name__ == "__main__":
    app.run(debug=True)



