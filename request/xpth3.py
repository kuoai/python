from lxml import etree
html = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
"""
html = etree.HTML(html)
result = html.xpath('//li[1]/ancestor::*')
result = html.xpath('//li[1]/ancestor::div')
result = html.xpath('//li[1]/attribute::*')
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
result = html.xpath('//li[1]/descendant::span')
result = html.xpath('//li[1]/following::*[2]')


print(result)