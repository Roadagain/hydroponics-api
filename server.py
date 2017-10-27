#!/usr/bin/env python3
#coding: utf-8

from flask import Flask, jsonify, make_response
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)

@app.route('/')
def hello():
    res = {'data': 'Hello'}
    return make_response(jsonify(res))

def main():
    app.run()

if __name__ == '__main__':
    main()
