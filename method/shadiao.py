import requests
class fool(object):

    def __init__(self):
        pass

    @property
    def chp(self):
        return requests.get('https://chp.shadiao.app/api.php').text
    
    @property
    def cnm(self):
        return requests.get('https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn').text

    @property
    def nmsl(self):
        return requests.get('https://nmsl.shadiao.app/api.php').text
