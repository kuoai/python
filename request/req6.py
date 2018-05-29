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

# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html ,re.S)
result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)      #search()会返回第一个符合条件的匹配目标
# search()方法的第三个参数都加了re.S,这使的.*?可以匹配换行，所以含有换行的li节点被匹配到了


# 由于代码有换行，所以这里第三个参数需要传入re.S
if result:
    print(result.group())
    print(result.group(1),result.group(2))