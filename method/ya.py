import json
import random


def loadjson(path):
    f=open(path,'r',encoding='utf-8')
    json_out=json.load(f)
    f.close()
    return json_out
    
class _poem(object):
    def __init__(self):
        self.poem=loadjson('data/唐诗三百首.json')

    @property
    def gou(self):
        out=dict(random.sample(self.poem,1)[0])
        return [
                out['text'],'这首是'+out['author']+'的'+out['title']
                ]

class _lunyu(object):
    def __init__(self):
        self.lunyu=loadjson('data/lunyu.json')

    @property
    def all(self):
        a=[]
        for i in self.lunyu:
            for v in self.lunyu[i]:
                a=a+[self.lunyu[i][v]]
        return random.sample(a,1)[0]
    
    def search(self,txt):
        pass

class wenyan(object):
    def __init__(self):
        self.lunyu=_lunyu()
        self.poem=_poem()