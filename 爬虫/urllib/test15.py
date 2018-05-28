from urllib.parse import urlparse

# result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
# print(result)


# scheme:他是默认的协议(http/https等),假如这个链接没有带协议信息，会将这个作为默认的协议
# result = urlparse("http://www.baidu.com/index.html#comment", scheme="https")
# print(result)

# allow_fragments:是否忽略fragment,如果设置为False,fragment部分就会被忽略,它会被解析为path、parameters或者query的一部分，而fragment部分为空
# result = urlparse("http://www.baidu.com/index.html;user?id=5#comment",allow_fragments=False)
# result2 = urlparse("http://www.baidu.com/index.html#comment",allow_fragments=False)
# print(result)
# print(result2)

result = urlparse("http://www.baidu.com/index.html#comment",allow_fragments=False)
print(result.scheme,result[0],result.netloc,result[1],sep="\n")
