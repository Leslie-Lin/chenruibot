#coding=utf8
import json
import re
from webconnect.pyiotqq import PyIotqq
from webconnect.webapi import IotqqWebapi
from time import sleep, ctime
import threading
import text
from method import t_notice,t_crossout
from method.send import send,groupsend

#基本声明
file_setting=open ('config.json')
setting=json.load(file_setting)
file_setting.close()

#类实例化
pyiotqq = PyIotqq(setting['robotqq'], setting["socketio_url"], setting["socketio_path"], setting["webapi_url"])
webapi = pyiotqq.webapi

#方法-秘书服务-老板
def OnFriendMsgs(data):
    print(data)
    if 'CurrentPacket' in data:
        if data['CurrentPacket']['Data']['FromUin']==setting['masterqq']:
            a=text.main(data['CurrentPacket']['Data']['Content'])
            if a!=None:
                send(a,setting['masterqq'])
#方法-群机器人服务
def OnGroupMsgs(data):
    a=text.groupmain(data['CurrentPacket']['Data']['Content'],data['CurrentPacket']['Data']['FromGroupId'])
    if a!=None:
        groupsend(a,data['CurrentPacket']['Data']['FromGroupId'])

if __name__ == '__main__':
    pyiotqq.sio.on('OnFriendMsgs', OnFriendMsgs)
    pyiotqq.sio.on('OnGroupMsgs', OnGroupMsgs)
    sleep(1)
    t_notice.listener_notice()
    t1 = threading.Thread(target=t_notice.listener_notice)
    t2 = threading.Thread(target=t_crossout.crossout_notice)
    t1.start()
    t2.start()

