from django.conf.urls import url, include
from django.contrib import admin
from authentication.views import SuccessView

urlpatterns = [
    #url(r'^$', 'core.views.home', name='home'),
    url(r'^core/',  include('core.urls')),
    url(r'^blog/',  include('blog.urls')),
    url(r'^help/',  include('help.urls')),
    url(r'^polls/', include('polls.urls')),
    #url(r'^users/', include('users.urls')),
    url(r'^authentication/', include('authentication.urls')),
    #url(r'^polls/search/', include('haystack.urls')),
    url(r'^admin/', admin.site.urls),
]
