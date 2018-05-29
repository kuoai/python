import requests
from requests.packages import urllib3

urllib3.disable_warnings()
# SSL证书验证，当发送HTTP请求的时候，他会检查SSL证书，我们可以用verify参数控制是否查此证书，如果不加verify参数的话，会默认True，会自动验证
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 如果请求一个HTTPS站点，但是证书验证错误的页面时，则会报错
# response = requests.get('https://www.12306.cn', verify=False)