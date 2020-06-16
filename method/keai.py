import requests
import random
class cute(object):
    def __init__(self):
        pass
    
    @property
    def cat(self):
        r = requests.get('https://api.thecatapi.com/v1/images/search')
        return r.json()[0]['url']
    
    @property
    def ak12(self):
        r = ['https://ae01.alicdn.com/kf/Haa3b6b918f1e455e82338f38f29d74c5B.jpg',
            'https://ae01.alicdn.com/kf/H2c17d39791a04367a5762068316d87500.jpg',
            'https://ae01.alicdn.com/kf/H92c49304aaff4da9b709d524d991b7d8a.jpg',
            'https://ae01.alicdn.com/kf/H53d6717337ce48509bd0ecd3f47cf6daE.jpg',
            'https://ae01.alicdn.com/kf/Hfb08534ed4204220aad8cf6a3b6c5249Q.jpg',
            'https://ae01.alicdn.com/kf/H87218ecf16e645f0a3342359b3613f75h.jpg',
            'https://ae01.alicdn.com/kf/H87ba47dcd85948e2abe1dd5633fdf75f7.jpg',
            'https://ae01.alicdn.com/kf/He72632b6268b462f85afaf89a8d935aez.jpg',
            'https://ae01.alicdn.com/kf/H93f82f4a7e494df88456fdbd5dc96d8bc.jpg',
            'https://ae01.alicdn.com/kf/H22ee9fede3334274a7056853125b589aS.jpg',
            'https://ae01.alicdn.com/kf/Hfc9479b6daeb4a2cbea2d0f4221dcf2fs.jpg',
            'https://ae01.alicdn.com/kf/Hb24b9a89565c4dfba6116d901717c0b8a.jpg',
            'https://ae01.alicdn.com/kf/H801fa976cbdc4641a37527c7587f7987b.jpg',
            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589340471392&di=044f96a62551cfb58737c889e6ee582d&imgtype=0&src=http%3A%2F%2Fimg.nga.178.com%2Fattachments%2Fmon_201808%2F25%2F-7Q5-jud7ZeT3cS10a-nw.jpg',
            'https://i0.hdslb.com/bfs/article/96c9c6ce9af5088dfb475100c8b588e3a6580e15.jpg',
            'https://i0.hdslb.com/bfs/article/15eef38e152b4720d65b76f2ed8cbfc7191ed8f7.jpg',
            'https://i0.hdslb.com/bfs/article/83af1d495b98d29af59833f985f7ba2a62c6b927.jpg',
            'https://i0.hdslb.com/bfs/article/2619f0a597e455f6bf39a46055d85fc97d7a42e0.jpg']
        return random.sample(r,1)[0]



    @property
    def xian(self):
        r = ['https://i.loli.net/2020/06/09/B1Szjeg5G36sXux.jpg',
             'https://i.loli.net/2020/06/09/3ea4rMzlWhYmjA1.jpg',
             'https://i.loli.net/2020/06/09/57e1ib6QspyqKn4.jpg',
             'https://i.loli.net/2020/06/09/w9MBHxhb2sXJYnL.jpg',
             'https://i.loli.net/2020/06/09/nWDAmaiSfe3OV9s.jpg',
             'https://i.loli.net/2020/06/09/IPMXz6DhQyHrjmT.jpg',
             'https://i.loli.net/2020/06/09/LYoyJGuw8KzleUF.jpg',
             'https://i.loli.net/2020/06/09/txYCFu2LXpDJzRT.jpg',
             'https://i.loli.net/2020/06/09/cNY5iLTO6HVXP3M.jpg',
             'https://i.loli.net/2020/06/09/CNsZP7yrD1LQedt.jpg',
             'https://i.loli.net/2020/06/09/OQmDBf5eUiyHLuM.jpg',
             'https://i.loli.net/2020/06/09/REiQfqFxv48aTtL.jpg',
             'https://i.loli.net/2020/06/09/T7kXDxQ2YcjB6mW.jpg',
             'https://i.loli.net/2020/06/09/4ejmSiOBYp2lzwH.jpg',
             'https://i.loli.net/2020/06/09/54d7cfZgoyvkNXY.jpg',
             'https://i.loli.net/2020/06/09/qhszDFt3Ov6Pi7l.jpg',
             'https://i.loli.net/2020/06/09/7Nqtm6Rr5Bd8gzA.jpg',
             'https://i.loli.net/2020/06/09/4HMFsPmYwyUG1IW.jpg',
             'https://i.loli.net/2020/06/09/ykbELqK8M1mAoiV.jpg'
             ]
        return random.sample(r,1)[0]
    @property
    def tongnai(self):
        url='https://tongnai.oss-cn-beijing.aliyuncs.com/tongnai/{0}'
        list_filename=[
                'kimo/kimo1-1.wav','kimo/kimo12-1.wav','kimo/kimo4-1.wav','kimo/kimo2-1.wav','kimo/kimo7-1.wav','kimo/kimo10-1.wav','kimo/kimo9-1.wav','kimo/kimo1-2.wav',
                'hentai/hentai4-1.wav','hentai/hentai1-1.wav','hentai/hentai4-1.wav','hentai/hentai9-1.wav','hentai/hentai9-2.wav',
                'baka/baka9-1.wav','baka/baka12-1.wav','baka/baka15-1.wav','baka/baka9-2.wav','baka/baka12-2.wav','baka/baka2-1.wav','baka/baka1-1.wav','baka/baka6-1.wav',
                'urusai/urusai12-3.wav','urusai/urusai5-2.wav','urusai/urusai12-2.wav','urusai/urusai2-1a.wav','urusai/urusai5-1.wav','urusai/urusai4-1.wav','urusai/urusai9-1.wav','urusai/urusai2-1.wav','urusai/urusai12-1.wav'
            ] 
        a=url.format(random.sample(list_filename,1)[0])
        print(a)
        return a
    
    def pixiv_url(self,title, artworkid, author, artistid):  # 拼凑消息
        purl = "www.pixiv.net/artworks/" + str(artworkid)  # 拼凑p站链接
        uurl = "www.pixiv.net/users/" + str(artistid)  # 画师的p站链接
        msg = title + "\r\n" + purl + "\r\n" + author + "\r\n" + uurl
        return msg
    
    def setuapi_0(self,tag='', num=1, r18=False):
        url = 'http://api.yuban10703.xyz:2333/setu_v2'
        params = {'r18': r18,
                'num': num,
                'tag': tag}
        try:
            res = requests.get(url, params, timeout=5)
            setu_data = res.json()
            status_code = res.status_code
        except Exception as e:
            return e, '', 'boom~~'
        msg, filename = [], []
        if status_code == 200:
            print('从api获取到{0}条数据'.format(len(setu_data['data'])))  # 打印获取到多少条
            for i in setu_data['data']:
                msg.append(self.pixiv_url(i['title'], i['artwork'], i['author'], i['artist']))
                filename.append(i['filename'])
            url = 'https://cdn.jsdelivr.net/gh/laosepi/setu/pics/'+filename[0]
            return [r'/P I C'+url,msg[0]]
        elif status_code == 404:
            a=random.sample(['草','干','淦','艹','日'],1)[0]
            b=random.sample(['你的','老色批，你的','什么东西，你的','什么人啊，这'],1)[0]
            c=random.sample(['鸡巴','jb',''],1)[0]

            return '错误'+str(status_code)+'：\n我{0}{1}xp也太{2}怪了吧'.format(a,b,c)
        else:
            return '错误'+str(status_code)+'：\n您应该歇一歇'

    def setu(self,tag):
        if len(tag)==4:
            tag=''
        else:
            tag=tag[2:-2]
        return self.setuapi_0(tag=tag, num=1, r18=False)