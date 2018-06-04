from django.conf.urls import url

from . import view,search

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^search_form$', search.search_form),
    url(r'^search$', search.search),
]