import urllib.request
import urllib.parse

data=bytes(urllib.parse.urlencode({"word":"hello","aaa":"bbb"}),encoding="utf8")
response=urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read())

# 转字节流bytes