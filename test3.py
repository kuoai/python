import os
import requests
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool
GROUNP_START = 1
GROUNP_END=5
# 加载单个ajax请求的结果，其中唯一变化的就是offset，所以把他当做参数
def get_page(offset):
    parmas={
        "offset":offset,
        "format":"json",
        "keyword":"街拍",
        "autoload":"true",
        "count":"20",
        "cur_tab":"3",
        "from":"gallery",
    }
    url = "https://www.toutiao.com/search_content/?"+ urlencode(parmas)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
    except response