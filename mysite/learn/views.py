from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(u"<h1>你还年轻吗？<h1/>")