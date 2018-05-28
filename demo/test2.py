# -*- coding: utf-8 -*-
from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "今天是周三"
if __name__=="__name__":
    app.run()