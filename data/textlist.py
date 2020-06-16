#coding=utf8
import random
list_hentai=["你，你要做什么！","滚啊变态！","恶心，你想干什么？"]
list_some=['点','些','一点','一些','','']
def jingranshuru(a):
    aa=[random.choice(['','你']),
        random.choice(['竟然','居然']),
        random.choice(['输入','导入','用']),
        a]
    return ''.join(aa)
def texterror():
    aa=[random.choice(['这里','这个地方']),
        random.choice(["出错了",
                       "不对",
                       "看不懂诶",
                       "错了",
                       "".join(['有',random.choice(list_some),'问题'])
                       ]
                      )
        ]
    return ''.join(aa)
