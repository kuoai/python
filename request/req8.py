import re
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''
# content = "54aK54yr5oiR54ix5L2g"
# content = re.sub("\d+","",content)
# print(content)
# 这里只需要给第一个参数传入\d+来匹配所有的数字，第二个参数为替换成的字符串（如果去掉该参数的话，可以赋值为空），第三个参数是原字符串。

# results = re.findall('<li.*?>\s*?(\w+)(</a>)?\s*?</li>',html,re.S)
# for resu in results:
#     print(resu[0])


# sub()
# html = re.sub('<a.*?>|</a>',"",html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>',html,re.S)
# for result in results:
#     print(result.strip())



# compile()  这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
content1 = "2016-12-15 12:00"
content2 = "2016-12-17 12:55"
content3 = "2016-12-22 13:21"
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern,"",content1)
result2 = re.sub(pattern,"",content2)
result3 = re.sub(pattern,"",content3)
print(content1,content2,content3)

# 另外，compile()还可以传入修饰符，例如re.S等修饰符，这样在search()、findall()等方法中就不需要额外传了。所以，compile()方法可以说是给正则表达式做了一层封装，以便我们更好地复用。

