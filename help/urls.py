# coding: utf-8

from django.conf.urls import include, url
from . import views

app_name = 'help' # to differentiate the URL names(like index, detail,results) between different  apps
urlpatterns = [
    url(r'^$', views.articles , name='articles'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<slug>[-\w]+)/$', views.article, name='article'),
]
