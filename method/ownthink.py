#coding=utf8
import requests
import json
from method.send import send

def ownthink(data):
    try:
        aaa=requests.get('填入你自己的API网址'+data,timeout=5)
    except requests.exceptions.Timeout:
        send('啊？')
        return ownthinktwice(data)
    else:
        return(json.loads(aaa.text)["data"]["info"]["text"])
        
def ownthinktwice(data):
    try:
        aaa=requests.get('填入你自己的API网址'+data,timeout=5)
    except requests.exceptions.Timeout:
        return '抱歉，我这里网络不太好，您能再说一遍吗？'
    else:
        return(json.loads(aaa.text)["data"]["info"]["text"])
