#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 17:58
# @Author  : yangmingming
# @Site    : 
# @File    : manage.py
# @Software: PyCharm

from flask_script import Manager, Server
from main import app

manager = Manager(app)
manager.add_command('server', Server())


@manager.shell
def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()
