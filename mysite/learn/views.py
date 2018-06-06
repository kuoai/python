from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(u"你还年轻吗？")