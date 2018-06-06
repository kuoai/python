from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


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


# 使用模板
def index(request):
    return render(request,"index.html")

# 跳转函数
def old_add2_redirect(request,a,b):
    return HttpResponsePermanentRedirect(
        reverse("add2",args=(a,b))
    )

def home(request):
    # list = ["java","html","js","css","python"];
    # list = {"site": u"百度", "content": u"百度一下，你就知道"};
    list = map(str,range(100))
    return render(request, "home.html",{"list": list})

def homeTest(request):
    return render(request,"homeTest.html")