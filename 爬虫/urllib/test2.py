import urllib.request
response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode("utf-8"))
print(type(response))
print(response.status)          #状态码
print(response.getheaders())        #响应的头信息
print(response.getheader("Server"))   #服务器是Nginx搭建

# 网页抓取函数
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)