import http.cookiejar,urllib.request
filename = "cookies.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)

# 要保存成LWP格式的Cookies文件，可以在声明时就改为
cookie = http.cookiejar.LWPCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_expires=True,ignore_discard=True)


# 这时CookieJar就需要换成MozillaCookieJar，他在生成文件时会用到，是CookieJar的子类，可以用来处理cookies的文件相关的事件
# 比如读取和保存Cookies，可以将Cookies保存成Mozilla型浏览器的Cookies格式。
# 另外，LWPCookieJar同样可以读取和保存Cookies，但是保存的格式和MozillaCookieJar不一样，它会保存成libwww-perl(LWP)格式的Cookies文件。