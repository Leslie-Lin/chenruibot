from webconnect.webapi import IotqqWebapi
import json
from time import sleep
file_setting=open ('config.json')
setting=json.load(file_setting)
file_setting.close()

robotqq=setting['robotqq']
masterqq=setting['masterqq']
webapi_url=setting["webapi_url"]

webapi = IotqqWebapi(webapi_url,robotqq)

def send(x,qqhao=masterqq):
    if type(x)==str:
        if x[0:6]=='/P I C':
            webapi.send_friend_pic_msg(qq=qqhao, pic_url=x[6:])
        elif x[0:6]=='/VOICE':
            webapi.send_friend_voice_msg(qq=qqhao, voiceUrl=x[6:])
        else:
            webapi.send_friend_text_msg(qq=qqhao, content=x)
    elif type(x)==int:
        sleep(x)
    elif type(x)==list:
        for i in x:
            send(i,qqhao)
            sleep(1)
    else:
        pass

def groupsend(x,qqhao=masterqq):
    if type(x)==str:
        if x[0:6]=='/P I C':
            webapi.send_group_pic_msg(group_id=qqhao, pic_url=x[6:])
        elif x[0:6]=='/VOICE':
            webapi.send_group_voice_msg(group_id=qqhao, voiceUrl=x[6:])
        else:
            webapi.send_group_text_msg(group_id=qqhao, content=x)
    elif type(x)==int:
        sleep(x)
    elif type(x)==list:
        for i in x:
            groupsend(i,qqhao)
            sleep(1)
    else:
        pass

def shutup(groupid,shutupid,time=10):
    return webapi.shut_up(groupid,shutupid,time)