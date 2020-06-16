#coding=utf8
import time
import datetime
import re
import itertools
import json
import calendar
import os

#年
s1=r'\d\d\d\d'
#日期
s2=r'(\d\d\.\d\d)'
#时：分
s3=r'\d\d:\d\d'
#默认时间
default_time=['07','00']
#汉数字转化
def tr_zn_to_digit(zn):
    d_zn_to_digit = {
        "零": 0,"一": 1,"二": 2,"两": 2,"三": 3,"四": 4,"五": 5,"六": 6,"七": 7,"八": 8,"九": 9,"十": 10,"百": 100,"千": 1000,"万": 10000,"亿": 100000000,
    }
    for e in zn:
        if e not in zn:
            raise ValueError('传入值含未知字符')
    ores = 0
    ures = 0

    o = zn.split('亿')
    if len(o) == 1:
        o = ['', o[0]]
    for i, e in enumerate(o):
        res = 0
        for j, char in enumerate(e):
            if char in d_zn_to_digit:

                if char in '十百千':
                    if not ((j == 0 or e[j - 1] in '零十百千万') and char == '十'):
                        continue
                elif char in '万':
                    res *= d_zn_to_digit[char]
                    continue
                cur_digit = d_zn_to_digit[char]

                if j < len(e) - 1:
                    next_char = e[j + 1]
                    if next_char in '十百千':
                        cur_digit *= d_zn_to_digit[next_char]
                res += cur_digit
        if i == 0:
            ores = res * 100000000
        elif i == 1:
            ures = res
    res = ores + ures
    return res

#汉字对照表
def mttime(a):
    mt = datetime.datetime.now() + datetime.timedelta(days=1)
    return mt.strftime(a)

def httime(a):
    ht = datetime.datetime.now() + datetime.timedelta(days=2)
    return ht.strftime(a)

def getNextXday(X):
    d={1:calendar.MONDAY,2:calendar.TUESDAY,3:calendar.WEDNESDAY,4:calendar.THURSDAY,5:calendar.FRIDAY,6:calendar.SATURDAY,7:calendar.SUNDAY}
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    m1 = d[X]
    while today.weekday() != m1:
        today += oneday
    nextXday=[today.strftime('%Y'),today.strftime('%m'),today.strftime('%d'),None,None]
    return nextXday

def timetable():
    a={'明天':[mttime('%Y'),mttime('%m'),mttime('%d'),None,None],
              '后天':[httime('%Y'),httime('%m'),httime('%d'),None,None],
              '早上':[None,None,None,'07','00'],
              '白天':[None,None,None,'10','00'],
              '中午':[None,None,None,'12','00'],
              '下午':[None,None,None,'15','00'],
              '晚上':[None,None,None,'19','00'],
              '半夜':[None,None,None,'23','00'],
              '下周':getNextXday(1),
              '下周一':getNextXday(1),
              '下周二':getNextXday(2),
              '下周三':getNextXday(3),
              '下周四':getNextXday(4),
              '下周五':getNextXday(5),
              '下周六':getNextXday(6),
              '下周日':getNextXday(7)
              }
    return a
def hanzicheck(str_time,list_time):
    dt=datetime.datetime.now()
    str_time=str_time.replace('后','')
    str_time=str_time.replace('明早','明天早上')
    str_time=str_time.replace('明晚','明天晚上')
    str_time=str_time.replace('小时','时')
    str_time=str_time.replace('分钟','分')
    str_time=str_time.replace('日','天')
    str_time=str_time.replace('星期','周')
    str_time=str_time.replace('上午','白天')
    #------------------
    dict_shijian=timetable()
    checked=False
    for k in dict_shijian:
        check=re.compile(k)
        if check.search(str_time):
            checked=True
            v=dict_shijian[k]
            for i in range(len(v)):
                if v[i]!=None:
                    list_time[i]=v[i]
    '''
    if checked:
        return list_time
    '''
    sj='[零一两二三四五六七八九十百千万亿]+[时分天周月]'
    if re.findall(sj,str_time)!=[]:
        sz='[零一两二三四五六七八九十百千万亿]*'
        ssz=re.compile(sz)
        hanshuzi=re.findall(ssz,str_time)
        while '' in hanshuzi:
            hanshuzi.remove('')
        for i in hanshuzi:
            str_time=str_time.replace(i,str(tr_zn_to_digit(i)))
        sz_sj='[0-9]*[\u4e00-\u9fa5]*'
        ssz_sj=re.compile(sz_sj)
        list_sz_sj=re.findall(ssz_sj,str_time)
        while '' in list_sz_sj:
            list_sz_sj.remove('')
        list_alltime=time_add(list_sz_sj)
        if list_alltime==False:
            return ['aa','aa','aa','aa','aa']
        seconds=sum(list_alltime)

        if seconds % (3600*24) == 0:
            ht = dt + datetime.timedelta(days=seconds / (3600*24))
            list_time[0]=ht.strftime('%Y')
            list_time[1]=ht.strftime('%m')
            list_time[2]=ht.strftime('%d')
        else:
            ht = dt + datetime.timedelta(seconds=seconds)
            list_time[0]=ht.strftime('%Y')
            list_time[1]=ht.strftime('%m')
            list_time[2]=ht.strftime('%d')
            list_time[3]=ht.strftime('%H')
            list_time[4]=ht.strftime('%M')
    return list_time

def time_add(list_sz_sj):
    dt=datetime.datetime.now() #创建一个datetime类对象
    for i in range(len(list_sz_sj)):
        num=re.findall('[0-9]*',list_sz_sj[i])
        while '' in num:
            num.remove('')
        num=int(num[0])
        unit=re.findall('[\u4e00-\u9fa5]*',list_sz_sj[i])
        while '' in unit:
            unit.remove('')
        timess=timeunit_to_num(unit[0])
        if timess==False:
            return False
        unit=int(timess)
        list_sz_sj[i]=num*unit
    return list_sz_sj


def timeunit_to_num(str_unit):
    if len(str_unit)!=1:
        return False
    str_unit=str_unit.replace('分','60')
    str_unit=str_unit.replace('时','3600')
    str_unit=str_unit.replace('天',str(3600*24))
    str_unit=str_unit.replace('周',str(3600*24*7))
    check=re.findall('\D',str_unit)
    if check==[]:
        return str_unit
    else:
        return False

def timecheck(timee):
    timee=timee.replace('两点','2:00')
    timee=timee.replace('下午1','13')
    timee=timee.replace('下午2','14')
    timee=timee.replace('下午3','15')
    timee=timee.replace('下午4','16')
    timee=timee.replace('下午5','17')
    timee=timee.replace('下午6','18')
    timee=timee.replace('晚上6','18')
    timee=timee.replace('晚上7','19')
    timee=timee.replace('晚上8','20')
    timee=timee.replace('晚上9','21')
    timee=timee.replace('晚上10','22')
    timee=timee.replace('晚上11','23')
    dt=datetime.datetime.now() #创建一个datetime类对象
    '''
    y=dt.strftime('%Y')
    M=dt.strftime('%m')
    d=dt.strftime('%d')
    h=dt.strftime('%H')
    m=dt.strftime('%M')
    s=dt.strftime('%S')
    '''
    #------------------读取时间
    list_time=[]
    ss1=re.compile(s1)
    ss2=re.compile(s2)
    ss3=re.compile(s3)
    if timee!='':
        list_time=list(map(matchtotime,[ss1.search(timee),ss2.search(timee),ss3.search(timee)]))

        if list_time[0]==None:
            list_time[0]=['aa']
        else:
            list_time[0]=[list_time[0]]
        if list_time[1]==None:
            list_time[1]=['aa','aa']
        else:
            a,b=list_time[1].split('.')
            list_time[1]=[a,b]
        if list_time[2]==None:
            list_time[2]=['aa','aa']
        else:
            aa,bb=list_time[2].split(':')
            list_time[2]=[aa,bb]
        list_time = list(itertools.chain.from_iterable(list_time))
        list_time=hanzicheck(timee,list_time)
        return list_time
    else:
        return False
def matchtotime(a):
    if a!=None:
        return a[0]
    else:
        return None
    
def addnotice(data):
    list_json=[]
    dt=datetime.datetime.now()
    timee,content=data.split("提醒我", 1)
    if content=='':
        return '您要做什么？'
    list_time=timecheck(timee)
    if list_time:
        if list_time ==['aa','aa','aa','aa','aa']:
            return('什么时候提醒您？')
        if list_time[0]=='aa':
            list_time[0]=dt.strftime('%Y')
        if list_time[2]=='aa':
            dt=datetime.datetime.now()
            list_time[1]=dt.strftime('%m')
            list_time[2]=dt.strftime('%d')
        if list_time[4]=='aa':
            list_time[3]=default_time[0]
            list_time[4]=default_time[1]
        timeArray = time.strptime(str(list_time), "['%Y', '%m', '%d', '%H', '%M']")
        timeStamp = int(time.mktime(timeArray))
        dictn=[{'time':list_time,'timestamp':timeStamp,'content':content}]
        if os.path.exists('data/notice.json'):
            with open('data/notice.json', 'r') as f:
                list_json=json.load(f)
                f.close()
        list_json=list_json+dictn
        with open('data/notice.json', 'w+') as f:
            json.dump(list_json,f)
            f.close()
        return('遵命,将在'+list_time[0]+'年'+list_time[1]+'月'+list_time[2]+'日'+list_time[3]+'时'+list_time[4]+'分提醒您'+content)
    else:
        return('什么时候提醒您？')

def filternotice(cmd):
    list_json=[]
    cmd=cmd.replace('的','')
    cmd=cmd.replace('关于','')
    a,cmd=cmd.split("查看", 1)
    cmd,a=cmd.rsplit('提醒',1)
    if os.path.exists('data/notice.json'):
        with open('data/notice.json', 'r') as f:
            list_json=json.load(f)
            f.close()
    else:
        with open('data/notice.json', 'w+') as f:
            f.close()
    fil=filtern(cmd,list_json)
    if len(fil)==0:
        return '未找到相关提醒'
    else:
        out=[] 
        for i in fil:
            out=out+[time.strftime("%Y-%m-%d %H:%M", time.localtime(i['timestamp']))+','+i['content']]
        return out
    
def removenotice(cmd):
    list_json=[]
    cmd=cmd.replace('的','')
    cmd=cmd.replace('关于','')
    a,cmd=cmd.split("删除", 1)
    cmd,a=cmd.rsplit('提醒',1)
    if os.path.exists('data/notice.json'):
        with open('data/notice.json', 'r') as f:
            list_json=json.load(f)
            f.close()
    else:
        with open('data/notice.json', 'w+') as f:
            f.close()
    out=filtern(cmd,list_json)
    delnum=len(out)
    if len(out)==0:
        return '未找到相关的提醒，因此不需要删除'
    else:
        for i in out:
            if i in list_json:
                list_json.remove(i)
            with open('data/notice.json', 'w+') as f:
                json.dump(list_json,f)
                f.close()
        return '已删除'+str(delnum)+'条提醒'

def filtern(cmd,data):
    list_time = timecheck(cmd)
    out=[]
    if list_time and list_time!=['aa','aa','aa','aa','aa']:
        for i in data:
            list_check=[0,0,0,0,0]
            for nn in range(5):
                if list_time[nn]==i['time'][nn] or list_time[nn]=='aa':
                    list_check[nn]=True
            if list_check==[True,True,True,True,True]:
                out=out+[i]
    elif cmd=='所有'or cmd=='全部':
        out=data
    else:
        for i in data:
            if cmd==i['content']:
                out=out+[i]
    return out
