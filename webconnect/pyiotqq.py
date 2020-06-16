#coding=utf8
import socketio
from time import sleep, ctime
import requests
from webconnect.webapi import IotqqWebapi

dict_msgs={}
class PyIotqq:
    def __init__(self, robotqq: str, socketio_url: str, socketio_path: str, webapi_url: str):
        self.robotqq = robotqq
        self.sio = socketio.Client()
        self.sio.connect(socketio_url, socketio_path=socketio_path, transports=['websocket'])
        self.sio.event(self.connect)
        self.webapi = IotqqWebapi(webapi_url, robotqq)

    def connect(self):
        print('connected to server')
        self.sio.emit('GetWebConn', self.robotqq)  # 取得当前已经登录的QQ链接

        while True:
            self.sio.emit('GetWebConn', self.robotqq)
            self.webapi.keep_alive()
            sleep(30)
