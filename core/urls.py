from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


# Using Generic View
app_name = 'core' # to differentiate the URL names(like index, detail,results) between different  apps
urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='core/about.html'), name='about'),

    #url(r'^signup/$',  views.SignUpView.as_view(), name='signup'),
    #url(r'^signin/$',  views.SignInView.as_view(), name='signin'),
    #url(r'^signout/$', views.SignOutView.as_view(), name='signout'),
    #url(r'^reset/$',   views.ResetView.as_view(), name='reset'),
    #url(r'^success/$', views.SuccessView.as_view(), name='success'),
]
