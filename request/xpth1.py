from lxml import etree
# lxml提供了非常简明的路径选择表达式
# nodename,选取此节点的所有子节点
# / 从当前节点选取直接子节点
# // 从当前节点选取子孙节点
# . 选取当前节点
# .. 选取当前节点的父节点
# @选取属性

# title[@leng="eng"]        代表选择所有名称为title，同时属性lang的值为eng的节点

text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
"""
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode("utf-8"))

# 使用tostring()方法即可输出修正后的HTML代码，但是结果是bytes类型，利用decode()方法将其转成str类型