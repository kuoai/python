from django.shortcuts import render
from django.http import HttpResponse


# 第一种方法采用 /add/?a=4&b=5 这样GET方法进行
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) * int(b)
    return HttpResponse(str(c))


# 第二种方法 采用 /add/3/4/ 这样的网址的方式
def add2(request,a,b):
    c = int(a) * int(b)
    return HttpResponse(str(c))