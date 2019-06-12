#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time     : 6/11/2019 16:49
# @Author   : mingfei.net@gmail.com
# @FileName : day02.py
# @GitHub   : https://github.com/thu/project-0610

import mysql.connector
from collections import Iterable

config = {'user':'root', 'password':'system'}

connection = mysql.connector.connect(**config)

print(connection)

cursor = connection.cursor()

cursor.execute('show databases')

print(isinstance(cursor, Iterable))

for db in cursor:
    print(db)

print('-------------')

cursor.execute('select * from scott.dept')

rows = cursor.fetchall()

for row in rows:
    print(row)