#coding=utf8
import time
import datetime
import re
import itertools
import json
import calendar
import os

def addnotice(data):#格式：[json(y,m,d,week,clock)]提醒（QQ号）（做什么事）
    timee,content=data.split("提醒", 1)
    day,clock=timee.split("的",1)
