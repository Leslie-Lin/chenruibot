#coding=utf8
import numpy as np
import time
import datetime
from data.textlist import list_hentai,jingranshuru,texterror

def calculate(a):
    if 'import' in a:
        fucklist=list(map(lambda x:jingranshuru('import')+'，'+x,list_hentai))+["e...eval不行...import也不行..."]
        return fucklist[int(np.random.rand()*len(fucklist))]
    if 'eval' in a:
        fucklist=list(map(lambda x:jingranshuru('eval')+'，'+x,list_hentai))+["e...eval不行...import也不行..."]
        return fucklist[int(np.random.rand()*len(fucklist))]
    try:
        out=str(eval(a))
    except Exception as e:
        out=[texterror(),repr(e)]
    return out
