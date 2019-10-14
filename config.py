#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 15:03
# @Author  : yangmingming
# @Site    : 
# @File    : config.py
# @Software: PyCharm


class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
