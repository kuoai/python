from urllib.parse import urlparse
result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(type(result),result)

# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)

