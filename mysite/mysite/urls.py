from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views  # new


urlpatterns = [
    url(r'^index$',learn_views.index),
    url(r'^add/$', learn_views.add, name='add'),  # 注意修改了这一行

    url(r'^add/(\d+)/(\d+)/$', learn_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$',learn_views.add2, name='add2'),

    url(r"^home$", learn_views.home),
    url(r"^homeTest$",learn_views.homeTest),
    url(r'^form',learn_views.form),
    url(r'^ajax$', learn_views.ajax)

    # url(r'^admin/', admin.site.urls),
]
