#coding=utf8
import time
import datetime
import os
import json
from method.send import groupsend
import threading
def crossout_notice():
    while True:
        clock=time.strftime("%a%H", time.localtime()) 
        print(clock)
        if clock=='Sat18'or clock=='Sun18':
            t_send = threading.Thread(target=groupsend,args=('/P I Chttps://s1.ax1x.com/2020/05/12/YNfxM9.jpg',190704998,))
            t_send.start()
        time.sleep(1)
