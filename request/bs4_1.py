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

html2 = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
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

# soup = BeautifulSoup(html,"lxml")
# print(soup.a.parent)
soup = BeautifulSoup(html2,"lxml")
# print(soup.find(name="ul"))
# print(type(soup.find(name="ul")))
# print(soup.find(class_="panel-body"))
# print(soup.select(".panel .panel-heading"))
# for ul in soup.select("ul"):
    # print(ul.select("li"))
    # print(ul["class"])
    # print(ul.attrs["id"])
    # 直接传入中括号和属性名，以及通过attrs属性获取属性值，都可以成功


for li in soup.select("li"):
    # 要获取文本，当然也可以用前面所讲的string属性。此外，还有一个方法，那就是get_text()
    print(li.string)
    print(li.get_text())

# Beautiful Soup
# 推荐使用lxml解析库，必要时使用html.parser
# 节点选择筛选功能弱但是速度快
# 建议使用find()或者find_all查询匹配单个结果或者多个结果
# 如果对css选择器熟悉的话，可以使用select()方法选择