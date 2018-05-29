import requests

# cookies
# requests.get("http://httpbin.org/cookies/set/number/123456789")
# r = requests.get("http://httpbin.org/cookies")
# print(r.text)

#session
s = requests.session()
s.get("http://httpbin.org/cookies/set/number/123456789")
r = s.get("http://httpbin.org/cookies")
print(r.text)

# 利用session可以做到模拟同一个会话而不用担心cookies的问题，通常用于模拟登陆之后再进行下一步的操作
