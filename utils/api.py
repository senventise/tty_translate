import json
import urllib
import random
import requests
from utils.loadConfig import get_key, get_id
from utils.myHash import str_md5

base_url = "https://fanyi-api.baidu.com/api/trans/vip/translate?"
key = get_key()
app_id = get_id()
salt = int(random.random()*10000000)


def translate(q, f, t):
    sign = str_md5((str(app_id)+q+str(salt)+key))
    d = {
        "q": q,
        "from": f,
        "to": t,
        "appid": app_id,
        "salt": salt,
        "sign": sign
    }
    url = base_url+urllib.parse.urlencode(d)
    # print("Final url is "+url)
    res = requests.get(url).text
    try:
        data = json.loads(res)["trans_result"]
    except json.decoder.JSONDecodeError:
        print("response error")
    return data[0]
