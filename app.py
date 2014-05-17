# -*- coding: utf-8 -*-
from flask import Flask  
app=Flask(__name__)

@app.route('/')  
def hello_world():  
    return "Hello World"

@app.route('/channel/<id>/')
def channel_get(id=None):
    if id:
        return "page html %s" % id

if __name__ == '__main__':  
    app.run(host='61.160.251.17', port=3699)  
