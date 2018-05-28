from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote


# 实现了url的构造
# data = ["http","www.baidu.com","index.html","user","a=6","comment"]
# print(urlunparse(data))

# urlencode() 他在构造get请求的时候非常有用
# params = {
#     "name": "genmey",
#     "age": "22"
# }
# base_url = "hppt://www.baidu.com?"
# url = base_url + urlencode(params)
# print(url)


# 有了序列化，必然就有反序列化，如果我们有一串GET请求参数，利用parse_qs()方法，可以将他转为字典
# query = "name=anna&age=22"
# print(parse_qs(query))


# parse_qsl()方法，可将参数转化为元组组成的列表
# query = "name=anna&age=22"
# print(parse_qsl(query))


# quote()该方法可以将内容转化为URL编码的格式。URL中带有中文参数时，有时可能会导致乱码的问题，此时用这个方法可以将中文字符转化为URL编码
# keyword = "壁纸"
# url = "https://www.baidu.com/s?wd=" + quote(keyword)
# print(url)


# 进行URL解码
url = "https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8"
print(unquote(url))




