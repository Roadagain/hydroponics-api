#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = 'Hello'
    title = 'Welcome'
    return render_template('index.html', message=message, title=title)

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
