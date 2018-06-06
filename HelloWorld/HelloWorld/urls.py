from django.conf.urls import url

from . import view,search,search_post
from django.contrib import admin

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^search_form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search_post$',search_post.search_post),
    url(r'^admin/',admin.site.urls)
]