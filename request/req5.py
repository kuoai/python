import re
content = "Hello 123 4567 World_This is a Regex Demo"
result = re.match("^Hello.*4567",content)
result2 = re.search("123.*4567",content)
print(result.group())
print(result2.group())

content2 = "54aK54yr5oiR54ix5L2g"
content2 = re.sub("\d+","",content2)        #把所有的数字替换为空
print(content2)

# group()方法可以输出匹配到的内容
# span()方法可以输出匹配的范围，就是匹配到的结果字符串在原字符串中的位置范围
