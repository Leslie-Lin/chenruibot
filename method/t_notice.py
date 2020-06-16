#coding=utf8
import time
import datetime
import os
import json
from method.send import send
import threading
def listener_notice():
    while True:
        a=listenonce()
        if a!=[]:
            out=[]
            for i in range(len(a)):
                check=a[i].replace('，强提醒','')
                if check==a[i]:
                    out=out+[a[i]]
                else:
                    out=out+[check,1,check,1,check]
            t_send = threading.Thread(target=send,args=(out,))
            t_send.start()
        time.sleep(30)

def listenonce():
    list_out=[]
    timenow=time.time()
    time.sleep(1)
    if os.path.exists('data/notice.json'):
        with open('data/notice.json', 'r') as f:
            list_json=json.load(f)
            f.close()
    for i in list_json:
        if i['timestamp']<timenow:
            list_json.remove(i)
            list_out=list_out+[i]
    with open('data/notice.json', 'w+') as f:
        json.dump(list_json,f)
    f.close()
    out=[]
    for i in list_out:
        out=out+['别忘了'+i['content']+'哦']
    return out
