# cookie的处理就需要相关的Handker
import http.cookiejar,urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
for item in cookie:
    print(item.name+"="+item.value)

# 首先声明一个CookieJar对象，接下来需要利用HTTPCookieProcessor来构建一个handler，最后利用build_opener方法构建出opener，执行open()函数即可