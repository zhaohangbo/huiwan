from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^authentication/', include('authentication.urls')),
    #url(r'^polls/search/', include('haystack.urls')),
    url(r'^admin/', admin.site.urls),
]
