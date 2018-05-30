from lxml import etree
html = etree.parse("html.html",etree.HTMLParser())
result = html.xpath("//*")
result = html.xpath("//li")
result = html.xpath("//li")[0]
result = html.xpath("//li/a")

result = html.xpath('//a[@href="link4.html"]/../@class')
# parent::来获取父节点
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')

result = html.xpath('//li[@class="item-0"]')

result = html.xpath('//li[@class="item-0"]/a/text()')

result = html.xpath('//li/a/@href')

# 多属性匹配
text = """<li class="li li-first" name="item"><a href="link.html">first item</a></li>"""
html2 = etree.HTML(text)
result = html2.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)