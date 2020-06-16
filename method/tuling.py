import requests as r
import json
def tuling(a):
    data={
        "reqType":0,
        "perception": {
            "inputText": {
                "text": a
            },
            "selfInfo": {
                "location": {
                    "city": "北京"
                }
            }
        },
        "userInfo": {
            "apiKey": "193d85908a094ce2bc49d591bf904f5b",
            "userId": "564057"
        }
    }
    a=r.post('http://openapi.tuling123.com/openapi/api/v2',json=data)
    return(json.loads(a.text)['results'][0]['values']['text'])
