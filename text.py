#coding=utf8
import re
import random
from method import notice,ownthink,calculate,ya,keai,shadiao,send
re_addnotice=re.compile('.*?提醒我.*', re.I)
re_removenotice=re.compile('(删|移)除.*提醒', re.I)
re_filternotice=re.compile('(查看.*提醒)',re.I)
re_coffee=re.compile('(帮|给)我(泡|冲)*咖啡',re.I)
re_calculate=re.compile('(^计算)',re.I)
#附庸风雅
re_ya_gou=re.compile('(.我)?(念|读|来)一?首?句?段?诗',re.I)
re_ya_lunyu=re.compile('(.我)?(念|读|来)一?首?句?段?论语',re.I)
re_ya_lunyu_search=re.compile('论语里?(关于)?(.*?)的.*?',re.I)#这里匹配并传送到ya.py的程序还没有写完
#可爱
re_miao=re.compile('(猫|喵)+图',re.I)
re_ak12=re.compile('((((A|a)(K|k))(12)|(十二))|(ain))',re.I)
re_xian=re.compile('闲某色图',re.I)
re_tongnai=re.compile('让妹子骂我',re.I)
re_setu=re.compile('来张.*色图',re.I)
#傻屌
re_chp=re.compile('(夸+我)|(爱我)',re.I)
re_cnm=re.compile('(骂+我)|(嘴臭)',re.I)
re_nmsl=re.compile('(骂+我妈)|(草|操我)|(.*妈死.*)|(nmsl)|(.*你妈.*)|(.*傻逼.*)|(.*废物.*)|(.*脑瘫.*)',re.I)
re_jinyan=re.compile('抽奖|幸运抽奖')
re_russia=re.compile('俄罗斯轮盘')
#__init__
wenyan=ya.wenyan()
fool=shadiao.fool()
cute=keai.cute()
russia=[]

def main(data):
    if re_addnotice.search(data):
        return notice.addnotice(data)
    if re_removenotice.search(data):
        return notice.removenotice(data)
    if re_filternotice.search(data):
        return notice.filternotice(data)
    if re_coffee.search(data):
        return ['好的，请稍等',5,'您的咖啡已经泡好']
    if re_calculate.search(data):
        return calculate.calculate(data[2:])
    bot= tongyong(data,850682892)
    if bot=='我听不懂你说什么':
        return ownthink.ownthink(data)
    else:
        return bot

def groupmain(data,Msgbody):
    global russia
    if len(data)<4:
        return None
    if data[0:2]=='陈睿':
        data=re.sub(re.compile(',|\.|;|:|，|。|；|：',re.I),'',data)
        print(data)
        data=data[2:].strip()
    else:
        return None
    #----------------处理完成，下文为群专属功能----------------------
    #-------------禁言转盘-------------------
    if re_jinyan.match(data):
        best=random.random()
        if best<0.05:
            return '头奖！这位群友将不会被禁言'
        else:
            time=random.random()
            time=int(100-time**0.5*100)
            send.shutup(Msgbody['CurrentPacket']['Data']['FromGroupId'],Msgbody['CurrentPacket']['Data']['FromUserId'],time)
            return '幸运群友{}获得了{}分钟的禁言，我们一起来恭喜他'.format(Msgbody['CurrentPacket']['Data']['FromNickName'],time)
    #-------------俄罗斯轮盘赌---------------------------
    if re_russia.match(data):
        print(russia)
        russia.append([Msgbody['CurrentPacket']['Data']['FromGroupId'],Msgbody['CurrentPacket']['Data']['FromUserId'],Msgbody['CurrentPacket']['Data']['FromNickName']])
        check=[one for one in russia if one[0]==Msgbody['CurrentPacket']['Data']['FromGroupId']]
        if len(check)>=6:
            russia = [i for i in russia if i not in check]
            kill=random.choice(check)
            send.shutup(kill[0],kill[1],10)
            return kill[2]+'被枪毙了。'
        else:
            return Msgbody['CurrentPacket']['Data']['FromNickName']+'加入了决斗'
    return tongyong(data,Msgbody['CurrentPacket']['Data']['FromGroupId'])

def tongyong(data,qq):
    if data=='帮助':
        a='"陈睿，帮助"获得帮助\n"陈睿，抽奖"进行幸运抽奖，随机被禁言一定时间（需要使用者能被陈睿禁言）\n"陈睿，俄罗斯轮盘"参加俄罗斯轮盘赌（需要使用者能被陈睿禁言）\n"陈睿，喵喵图"获得猫图\n"陈睿，念诗"让让睿总念诗\n"陈睿，念论语"让陈睿念论语\n"陈睿，让妹子骂我"听妹子骂人\n"陈睿，夸夸我"让陈睿对你发情\n"陈睿，嘴臭"让陈睿骂你lv1\n"陈睿，骂我妈"让陈睿骂你lv2"\n"陈睿，来张色图"一看就懂什么意思，对吧'
        if qq==718665461:
            return a+'\n"陈睿，AK12"嘲笑AIN悲惨的命运\n"陈睿，闲某色图"发送某位群友的色图'
        else:
            return a
    
    if re_chp.match(data):
        return fool.chp
    if re_cnm.match(data):
        return fool.cnm
    if re_nmsl.match(data):
        return fool.nmsl
#-----------------傻屌-------------------------------
    if re_ya_gou.match(data):
        return wenyan.poem.gou
    if re_ya_lunyu.match(data):
        return wenyan.lunyu.all
    #if re_ya_lunyu_search.search(data):
    #    return lunyu.search()
    if re_miao.match(data):
        return '/P I C'+cute.cat
    if re_ak12.match(data):
        return '/P I C'+cute.ak12
    if re_xian.match(data):
        return '/P I C'+cute.xian
    if re_tongnai.match(data):
        return '/VOICE'+cute.tongnai
    if re_setu.match(data):
        return '老色批，你怎么不对着群友冲啊'
    bot='我听不懂你说什么'
    return bot
