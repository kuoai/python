from pyquery import PyQuery as pq
import requests
# 像Beautiful Soup一样，初始化pyquery的时候，也需要传入HTML文本来初始化一个PyQuery对象。它的初始化方式有多种，比如直接传入字符串，传入URL，传入文件名，等等

# 字符串初始化
html = """
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
"""
# doc = pq(html)
# print(doc("li"))
# 这里首先引入PyQuery这个对象，取别名为pq,然后声明了一个长HTML字符串,并将其当作参数传递给PyQuery类，这样就成功完成了初始化

doc1 = pq(url='http://cuiqingcai.com')
doc2 = pq(requests.get("http://cuiqingcai.com").text)
# print(doc1("title"))
# print(doc2("title"))
# 除了传递URL，还可以传递本地的文件名，此时将参数指定为filename
doc3 = pq(filename="html.html")
# print(doc3("P").text())

doc = pq(html)
# print(doc("#container .list li"))
# print(type(doc("#container .list li")))

# find()方法会将符合条件的所有节点选择出来，结果的类型是PyQuery类型
# 如果我们只想查找子节点，那么可以用children()
# 获取某个祖先节点,parents(),parents()方法会返回所有的祖先节点
# 如想筛选出子节点中class为active的节点，可以向children()方法传入CSS选择器.active
# 我们可以用parent()方法来获取某个节点的父节点
# 如果要筛选某个兄弟节点，我们依然可以向siblings方法传入CSS选择器
li = doc(".list .item-1.active")
print(li.siblings(".active"))


