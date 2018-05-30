from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Hello</p>","lxml")
# print(soup.p.string)

html = """
<html><head><title>The Dormouse's story</title><title>hello</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,"lxml")
# print(soup.body.p.string)
# print(soup.prettify())
# prettify()这个方法可以把要解析的字符串以标准的缩进格式输出
# 调用soup.titlt.string,这实际上是输出HTML中的title节点的文本内容
# print(soup.title.name)
# print(soup.head.title)
# print(soup.p.attrs["class"])
# 可以利用string属性获取节点元素包含的文本内容
# print(soup.p.b.string)
# for i,child in enumerate(soup.body.children):
#     print(i,child)

soup = BeautifulSoup(html,"lxml")
print(soup.a.parent)
