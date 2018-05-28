from urllib import request
from bs4 import BeautifulSoup

url=r"http://www.jianshu.com"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page=request.Request(url,headers=headers)
page_info=request.urlopen(page).read().decode("utf-8")
soup=BeautifulSoup(page_info,"html.parser")
titles=soup.find_all("a","title")

# 第一种方式
try:
    file=open(r"D:\Python\test\b.txt","w")
    for title in titles:
        # 将爬到的文章题目写入txt中
        file.write(title.string+"\n")
finally:
    if file:
        file.close()

# 第二种方式
# with open(r'D:\Python\test\b.txt', 'w') as file:
#     for title in titles:
#         file.write(title.string + '\n')


# 'r'	以只读模式打开文件（默认模式）
# 'w'	以只写的方式打开文件，如果文件存在的话会先删除再重新创建
# 'x'	以独占的方式打开文件，如果文件已经存在则错误
# 'a'	以写的形式打开文件，若文件已存在，则以追加的方式写入
# 'b'	二进制模式
# 't'	文本模式（默认）
# '+'	更新文件（读/写）
# 打开的文件一定要关闭，否则会占用相当大的系统资源，所以对文件的操作最好使用try...finally...的形式


