# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/this-is-so-easy')
def ezpz():
    return 'ファックユーダジャエンゴ'
