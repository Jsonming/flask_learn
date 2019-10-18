#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 15:06
# @Author  : yangmingming
# @Site    : 
# @File    : main.py
# @Software: PyCharm

from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def home():
    return "hello word"


if __name__ == '__main__':
    app.run()
