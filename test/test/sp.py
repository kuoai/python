from urllib import request
from bs4 import BeautifulSoup       #BeautifulSoup是一个可以从html或者xml文件中提取节结构化数据的python库

# 构造头文件，访问浏览器
url=r"http://www.jianshu.com"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page=request.Request(url,headers=headers)
page_info=request.urlopen(page).read().decode("utf8")       #打卡url,获取HttpRequest返回对象并读取其ResponseBody
soup=BeautifulSoup(page_info,"html.parser")     #获取到的内容转成BeautifulSoup格式，并且将html.parser作为解析器
# print(soup.prettify())      #以格式化的形式打印html
titles=soup.find_all("a","title")       #查找所有a标签中class="title"的语句

# open()是读写文件的函数，with语句会自动close()已打开的文件
with open(r"D:\Python\test\a.txt","w") as file:
    for title in titles:
        file.write(title.string+"\n")
        file.write("http://www.jianshu.com"+title.get("href")+"\n\n")