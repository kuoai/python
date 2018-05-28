# 当请求中需要加入headers等信息时，就可以利用Request类来构建

import urllib.request
request = urllib.request.Request("https://python.org")
response = urllib.request.urlopen(request)
print(response.read().decode("utf8"))



# request的请求参数
# class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# 第一个参数url用于请求url，这是必传参数
# 第二个参数data如果要传，必须是bytes(字节流)类型的、如果他是字典，可以先用urllib.parse模块里的urlencode()编码
# 第三个参数是headers是一个字典，他就是请求头，我们可以在构造请求时通过headers参数直接构造，也可以通过调用请求实例的add_header()方法添加
# 添加请求头最常用的用法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是Python-urllib,我们可以通过修改他来伪装浏览器，比如要伪装火狐
# Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11
# 第四个参数origin_req_host指的是请求方的host名称或者IP地址
# 第五个参数unverifiable表示这个请求是否是无法验证的，默认是False，意思就是说用户没有足够权限来选择接收这个请求的结果。例如，我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，这时unverifiable的值就是True
# 第六个参数method是一个字符串，用来指示请求使用的方法，比如GET、POST和PUT等。
