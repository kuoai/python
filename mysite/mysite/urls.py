from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views  # new

urlpatterns = [
    url(r'^$',learn_views.index, name="home"),
    url(r'^add/$', learn_views.add, name='add'),  # 注意修改了这一行

    url(r'^add/(\d+)/(\d+)/$', learn_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$',learn_views.add2, name='add2'),


    url(r'^admin/', admin.site.urls),
]
