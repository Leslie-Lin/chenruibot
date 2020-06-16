import requests

def pixiv_url(title, artworkid, author, artistid):  # 拼凑消息
    purl = "www.pixiv.net/artworks/" + str(artworkid)  # 拼凑p站链接
    uurl = "www.pixiv.net/users/" + str(artistid)  # 画师的p站链接
    msg = title + "\r\n" + purl + "\r\n" + author + "\r\n" + uurl
    return msg

def setuapi_0(tag='', num=1, r18=False):
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
            msg.append(pixiv_url(i['title'], i['artwork'], i['author'], i['artist']))
            filename.append(i['filename'])
        url = 'https://cdn.jsdelivr.net/gh/laosepi/setu/pics/'+filename[0]
        return [r'/P I C'+url,msg[0]]
    else:
        return '错误'+str(status_code)+'：\n申请人色过头了'
