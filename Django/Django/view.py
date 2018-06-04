# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse("hello world!")


from django.shortcuts import render
def hello(request):
    context = {}
    context["hello"] = "你好"
    return render(request,"hello.html",context)

# 这里使用render()来代替之前的HttpResponse
# render()还使用了一个字典，context作为参数
# context字典元素的键值“hello”对应了模板中的变量{{hello}}

