
import pymongo
import os
from dotenv import load_dotenv
from flask import Flask, request


load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['flask-tutorial']


app = Flask(__name__)


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form['itemName']
    item_desc = request.form['itemDescription']
    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })
    return "Item submitted!"g


@app.route('/submit', methods=['POST'])
def submit():
    data = dict(request.json)
    collection.insert_one(data)
    return 'Data submitted nicely'


@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for i in data:
        print(i)
        del i['_id']
    # # return data

    data = {
        'data': data
    }
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
