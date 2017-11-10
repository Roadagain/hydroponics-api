#!/usr/bin/env python3
#coding: utf-8
"""The main program of hydroponics API server"""

from flask import Flask, jsonify, make_response, request
from pymongo import MongoClient

APP = Flask(__name__)
CLIENT = MongoClient('localhost', 27017)
DB = CLIENT.test_db
COLLECTION = DB.test_collection

@APP.route('/')
def hello():
    """Test response"""
    res = {'data': 'Hello'}
    return make_response(jsonify(res))

@APP.route('/update/<key>', methods=['POST'])
def update(key):
    """Update database from posted json"""
    data = request.json
    print(data)
    insert_res = COLLECTION.insert_one(data)
    res = {'result': insert_res.acknowledged}
    return make_response(jsonify(res))

@APP.route('/fetch/<key>', methods=['GET'])
def fetch(key):
    """Fetch data as a JSON from database"""
    data = []
    for i in COLLECTION.find():
        del i['_id']
        data.append(i)
    res = {'result': True, 'data': data}
    return make_response(jsonify(res))

def main():
    """Main function"""
    APP.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    APP.run()

if __name__ == '__main__':
    main()
