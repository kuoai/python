from urllib import request
from bs4 import BeautifulSoup
import time
import re

url="https://www.zhihu.com/question/22918070"
html=request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(html,"html.parser")      #解析器

# 用BeautifulSoup结合正则表达式来提取包含所有图片链接(img标签中，class="xxx",以jpg结尾的链接)的语句
links=soup.find_all("img","origin_image zh-lightbox-thumb",src=re.compile(r".jpg$"))
# print(links)

# 设置保存图片的路径,否则会保存到当前程序当前路径
path=r"D:\Python\test\images"       #路径前的r是保持字符串原始值的意思，就是说不对其中的字符串进行转义
# D:\Python\test\images是已存在的文件路径
for link in links:
    # print(link.attrs["src"])
    request.urlretrieve(link.attrs['src'],path+'\%s.jpg' % time.time())
# 使用request.urlretrieve直接将所有远程链接数据下载到本地
