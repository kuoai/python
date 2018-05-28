import urllib.request
url="http://www.douban.com/"        #网址
request=urllib.request.Request(url)     #请求
response=urllib.request.urlopen(request)        #爬取结果
data=response.read()
data=data.decode("utf-8")       #设置解码方式
print(data)         #打印结果
# 打印爬去网页的各类信息
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
