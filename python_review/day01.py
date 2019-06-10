#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time     : 6/10/2019 16:48
# @Author   : mingfei.net@gmail.com
# @FileName : day01.py
# @GitHub   : https://github.com/thu/project-0610

import os

# name = input('your name:')

# print(name)

with open('day01.py') as f:
    # print(type(f.readlines()))
    for line in f.readlines():
        # print(line.strip())
        pass

print([x for x in os.listdir('.') if os.path.isfile(x)])