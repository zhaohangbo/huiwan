# coding: utf-8

from django.conf.urls import url  
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.entries ,name='entries'),
    url(r'^(?P<slug>[-\w]+)/$', views.entry, name='entry'),
]
