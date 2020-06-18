import json
import re
from pyiotqq import PyIotqq
from time import sleep, ctime

def OnGroupMsgs(message):
    print("OnGroupMsgs", message)
    group_id = message["CurrentPacket"]["Data"]['FromGroupId']
    user_id = message["CurrentPacket"]["Data"]['FromUserId']
    content: str = message["CurrentPacket"]["Data"]['Content']
    nickname = message["CurrentPacket"]["Data"]['FromNickName']
    msg_type = message["CurrentPacket"]["Data"]['MsgType']
    msg_seq = message["CurrentPacket"]["Data"]['MsgSeq']
    group_name = message["CurrentPacket"]["Data"]['FromGroupName']


def OnFriendMsgs(message):
    print('OnFriendMsgs', message)

    user_id = message["CurrentPacket"]["Data"]['FromUin']
    content: str = message["CurrentPacket"]["Data"]['Content']


def OnEvents(message):
    print(message)
    msg_type = message["CurrentPacket"]["Data"]['EventMsg']['MsgType']
    if msg_type == 'ON_EVENT_GROUP_REVOKE':
        group_id = message["CurrentPacket"]["Data"]['EventData']['GroupID']
        AdminUserID = message["CurrentPacket"]["Data"]['EventData']['AdminUserID']
        UserID = message["CurrentPacket"]["Data"]['EventData']['UserID']
        if AdminUserID == UserID:  # 只发自己撤回自己的
            msg_seq = message["CurrentPacket"]["Data"]['EventData']['MsgSeq']
            content = "根据msg_seq从数据库获取对应消息的内容"
            if "\"tips\"" in content:
                # content_b = content
                content = json.loads(content)
                if content["tips"] == "[群图片]":
                    url = content["url"]
                    pic_hash = re.findall("[0-9A-Z]{32}", url)[0]
                    content = f"https://gchat.qpic.cn/gchatpic_new//--{pic_hash}/0"
                elif content["tips"] == "[小表情]":
                    content = content['Content']
                elif content["tips"] == "[大表情]":
                    return
                elif content["tips"] == "[AT消息]":
                    content = content['Content']
                elif content["tips"] == '[回复]':
                    content = content['ReplayContent']
                elif content["tips"] == "[语音]":
                    voice_url = content['url']
                    webapi.send_group_voice_msg(group_id, voice_url)
                    sleep(1)
                    content = "[语音消息](见上方)"
                else:
                    return

            nickname = "从内存或者数据库获取成员的nickname"
            content = f"{nickname}({UserID})撤回了一条信息：\n" + content
            print("content", content)
            webapi.send_group_text_msg(group_id, content)
    elif msg_type == 'ON_EVENT_GROUP_JOIN':
        group_id = message["CurrentPacket"]["Data"]['EventMsg']['FromUin']
        new_member_user_id = message["CurrentPacket"]["Data"]['EventData']['UserID']
        picUrl = f"https://q1.qlogo.cn/g?b=qq&nk={new_member_user_id}&s=640"
        webapi.send_group_pic_msg(group_id, picUrl, 2, content=f"欢迎新人[秀图40002]")


if __name__ == '__main__':
    robotqq = "2997815239"
    socketio_url = "http://182.92.197.153:8888/"
    socketio_path = '/socket.io'
    webapi_url = 'http://182.92.197.153:8888/v1/LuaApiCaller'
    pyiotqq = PyIotqq(robotqq, socketio_url, socketio_path, webapi_url)
    webapi = pyiotqq.webapi
    webapi.send_friend_text_msg(1919810, '114514')#该行可以给好友发消息，前面填QQ号
    pyiotqq.sio.on('OnGroupMsgs', OnGroupMsgs)
    pyiotqq.sio.on('OnEvents', OnEvents)
    pyiotqq.sio.on('OnFriendMsgs', OnFriendMsgs)
