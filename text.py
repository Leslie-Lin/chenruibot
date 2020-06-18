#coding=utf8
import re
from method import notice,ownthink,calculate,ya,keai,shadiao
re_addnotice=re.compile('.*?提醒我.*', re.I)
re_removenotice=re.compile('(删|移)除.*提醒', re.I)
re_filternotice=re.compile('(查看.*提醒)',re.I)
re_coffee=re.compile('(帮|给)我(泡|冲)*咖啡',re.I)
re_calculate=re.compile('(^计算)',re.I)
#附庸风雅
re_ya_gou=re.compile('(.我)?(念|读|来)一?首?句?段?诗',re.I)
re_ya_lunyu=re.compile('(.我)?(念|读|来)一?首?句?段?论语',re.I)
re_ya_lunyu_search=re.compile('论语里?(关于)?(.*?)的.*?',re.I)
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
#__init__
wenyan=ya.wenyan()
fool=shadiao.fool()
cute=keai.cute()

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
    bot= tongyong(data,114514)#有必要的话，把114514改成你的QQ
    if bot=='我听不懂你说什么':
        return ownthink.ownthink(data)
    else:
        return bot

def groupmain(data,qq):
    if len(data)<4:
        return None
    if data[0:2]=='陈睿':
        data=re.sub(re.compile(',|\.|;|:|，|。|；|：',re.I),'',data)
        print(data)
        data=data[2:].strip()
    else:
        return None
    return tongyong(data,qq)

def tongyong(data,qq):
    if data=='帮助':
        a='"陈睿，帮助"获得帮助\n"陈睿，喵喵图"获得猫图\n"陈睿，念诗"让让睿总念诗\n"陈睿，念论语"让陈睿念论语\n"陈睿，让妹子骂我"听妹子骂人\n"陈睿，夸夸我"让陈睿对你发情\n"陈睿，嘴臭"让陈睿骂你lv1\n"陈睿，骂我妈"让陈睿骂你lv2"'
        return a+'\n"陈睿，来张色图"一看就懂什么意思，对吧'
    
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
        return cute.setu(data)
    bot='我听不懂你说什么'
    return bot
