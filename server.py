#!/usr/bin/env python3
#coding: utf-8

from flask import Flask, jsonify, make_response, request
from pymongo import MongoClient
import json

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.test_db
co = db.test_collection

@app.route('/')
def hello():
    res = {'data': 'Hello'}
    return make_response(jsonify(res))

@app.route('/update/<key>', methods=['POST'])
def update(key):
    data = request.json
    print(data)
    insert_res = co.insert_one(data)
    res = {'result': insert_res.acknowledged}
    return make_response(jsonify(res))

@app.route('/show/<key>', methods=['GET'])
def show(key):
    data = []
    for i in co.find():
        del i['_id']
        data.append(i)
    res = {'result': True, 'data': data}
    return make_response(jsonify(data))

def main():
    app.run()

if __name__ == '__main__':
    main()
