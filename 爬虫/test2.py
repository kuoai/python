import os
import requests
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool

GROUP_START = 1
GROUP_END = 5

# 加载单个ajax请求的结果，其中唯一变化的就是offset，所以把他当作参数
def get_page(offset):
    parmas={
        'offset': offset,
        'format': 'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'3',
        'from': 'gallery',

    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(parmas)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

# 解析方法，提取每条数据的image_detail字段中的每一张图片链接，将图片链接和图片所属的标题一并返回，此时可以构造一个生成器
def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            # print(item)
            image_list = item.get('image_list')
            title = item.get('title')
            # print(image_list)
            for image in image_list:
                yield {
                    'image': image.get('url'),
                    'title': title
                }

# 保存
def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list','large')
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb')as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')

# 构造一个offset数组，遍历offset，提取图片链接，并将其下载
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()