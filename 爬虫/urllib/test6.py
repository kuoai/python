from urllib import request,parse
url = "http://httpbin.org/post"
header = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Host": "httpbin.org"
}
dect = {
    "name": "Germey"
}
data = bytes(parse.urlencode(dect),encoding="utf8")
req = request.Request(url=url,data=data,headers=header,method="POST")
# req = request.Request(url=url,data=data,method="POST")
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode("utf-8"))