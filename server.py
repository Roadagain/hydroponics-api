#!/usr/bin/env python3
#coding: utf-8

from flask import Flask, Response
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)

@app.route('/')
def hello():
    return Response(response = 'Hello', status = 200, content_type = 'text/plain')

if __name__ == '__main__':
    app.run()
