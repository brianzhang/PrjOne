# -*- coding: utf-8 -*-
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')  
def hello_world():  
    return "Hello World"

@app.route('/channel/<id>/')
def channel_get(id=None):
    if id:
        return render_template("index.html", data=id)

if __name__ == '__main__':  
    app.run(host='61.160.251.17', port=3690)  
