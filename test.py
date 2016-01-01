#!/usr/bin/env Python3
# -*- coding:utf-8 -*-

"""
@version: 0.1
@author: paranoidQ
@license: Apache Licence 
@contact: paranoid_qian@163.com
@file: test.py
@time: 16/1/1 14:37
"""

from SFEngine import *

engine = SFEngine()
engine.index('original')
engine.search('record/record0.wav')
engine.search('record/record8.wav')
