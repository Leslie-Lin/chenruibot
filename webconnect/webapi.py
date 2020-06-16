#coding=utf8
import requests
import json
import time

headers = {
    'Content-Type': 'application/json',
}
list_msg=[]
def print(*args, **kwargs):
    pass
class IotqqWebapi:
    def __init__(self, api_url: str, robotqq: str):
        self.api_url = api_url
        self.robotqq = robotqq

    # 瞎写的 keep-alive
    def keep_alive(self):
        r=requests.get(self.api_url)
        print(r.content)

    def _send_text_msg(self, toUser: int, content: str, sendToType: int):
        print("send_text_msg", toUser, content, sendToType)
        params = (
            ('qq', self.robotqq),
            ('funcname', 'SendMsg'),
        )

        data = {"toUser": toUser, "sendToType": sendToType, "sendMsgType": "TextMsg",
                "content": content, "groupid": 0, "atUser": 0, "replayInfo": None}
        print(json.dumps(data))
        response = requests.post(self.api_url, headers=headers,
                                 params=params, json=data)
        print(response.text)

    def _send_pic_msg(self, toUser, pic_url, sendToType, content='', fileMd5=""):
        print("send_pic_msg", toUser, pic_url, sendToType, content)
        params = (
            ('qq', self.robotqq),
            ('funcname', 'SendMsg'),
        )

        data = {"toUser": toUser, "sendToType": sendToType, "sendMsgType": "PicMsg", "content": content,
                "picUrl": pic_url, "groupid": 0, "atUser": 0, "picBase64Buf": "", "fileMd5": fileMd5}

        response = requests.post(self.api_url, headers=headers,
                                 params=params, json=data)
        print(response.text)

    def _send_xml_msg(self, toUser: int, xml_content: str, sendToType: int):
        print("send_text_msg", toUser, xml_content, sendToType)
        params = (
            ('qq', self.robotqq),
            ('funcname', 'SendMsg'),
        )

        data = {"toUser": toUser, "sendToType": sendToType, "sendMsgType": "XmlMsg",
                "content": xml_content, "groupid": 0, "atUser": 0, "replayInfo": None}
        print(json.dumps(data))
        response = requests.post(self.api_url, headers=headers,
                                 params=params, json=data)
        print(response.text)

    def send_reply_msg(self, group_id: str, content: str, reply_userid, raw_content, msg_seq=0):
        params = (
            ('qq', self.robotqq),
            ('funcname', 'SendMsg'),
            ('timeout', '10'),
        )

        data = {"toUser": group_id, "sendToType": 2, "sendMsgType": "ReplayMsg", "content": content, "groupid": 0,
                "atUser": 0,
                "replayInfo": {"MsgSeq": msg_seq, "MsgTime": int(time.time()), "UserID": reply_userid,
                               "RawContent": raw_content}}

        response = requests.post(self.api_url, headers=headers,
                                 params=params, data=json.dumps(data))
        print(response.text)

    def _send_voice_msg(self, toUser, sendToType, voiceUrl):
        params = (
            ('qq', self.robotqq),
            ('funcname', 'SendMsg')
        )

        data = {"toUser": toUser, "sendToType": sendToType, "sendMsgType": "VoiceMsg", "content": "", "groupid": 0,
                "atUser": 0, "voiceUrl": voiceUrl, "voiceBase64Buf": ""}

        response = requests.post(self.api_url, headers=headers,
                                 params=params, data=json.dumps(data))
        print(response.text)

    def send_friend_text_msg(self, qq: int, content: str):
        self._send_text_msg(toUser=qq, content=content, sendToType=1)

    def send_group_text_msg(self, group_id: int, content: str):
        self._send_text_msg(toUser=group_id, content=content, sendToType=2)

    def send_friend_pic_msg(self, qq: int, pic_url: str, content='', fileMd5=""):
        self._send_pic_msg(toUser=qq, pic_url=pic_url, sendToType=1, content=content, fileMd5=fileMd5)

    def send_group_pic_msg(self, group_id: int, pic_url: str, content='', fileMd5=""):
        self._send_pic_msg(toUser=group_id, pic_url=pic_url, sendToType=2, content=content, fileMd5=fileMd5)

    def send_friend_voice_msg(self, qq: int, voiceUrl: str):
        self._send_voice_msg(toUser=qq, sendToType=1, voiceUrl=voiceUrl)

    def send_group_voice_msg(self, group_id: int, voiceUrl: str):
        self._send_voice_msg(toUser=group_id, sendToType=2, voiceUrl=voiceUrl)

    # atUsers:list 要艾特的成员的qq号,qq号类型为str 如 ["123456","666666"]
    # content: 一连串艾特后面的消息内容
    def send_at_msg(self, group_id: int, atUsers: list, content: str = " "):
        at_content = ",".join(atUsers)
        content = f"[ATUSER({at_content})]{content}"
        self._send_text_msg(toUser=group_id, content=content, sendToType=2)

    def send_friend_xml_msg(self, qq, xml_content):
        self._send_xml_msg(toUser=qq, xml_content=xml_content, sendToType=1)

    def send_group_xml_msg(self, group_id, xml_content):
        self._send_xml_msg(toUser=group_id, xml_content=xml_content, sendToType=2)

    # brief  "[分享] xxx"
    # url  "https://example.com"
    # pic_url 显示的图片
    # title 标题
    # summary 内容
    @staticmethod
    def make_share_xml(brief, url, pic_url, title, summary):
        content = f'<?xml version=\'1.0\' encoding=\'UTF-8\' standalone=\'yes\' ?><msg serviceID="1" ' \
                  f'templateID="1" action="web" brief="{brief}" sourceMsgId="0" url="{url}" ' \
                  f'flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><picture cover="{pic_url}" w="0" h="0" />' \
                  f'<title>{title}</title><summary>{summary}</summary></item><source name="" icon="" ' \
                  f'url="http://url.cn/UQoBHn" action="app" a_actionData="com.tencent.mtt://{url}"' \
                  f' i_actionData="tencent100446242://{url}" appid="-1" /></msg>'
        return content
