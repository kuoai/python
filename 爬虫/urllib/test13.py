import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen("https://www.baidu.com",timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print("Time out")

# reason属性的结果是socket.timeout类,isinstance()方法来判断它的类型

