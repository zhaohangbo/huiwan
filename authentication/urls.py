from django.conf.urls import url

from . import views

"""
app_name = 'polls' # to differentiate the URL names(like index, detail,results) between different  apps
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
"""

# Using Generic View
app_name = 'authentication' # to differentiate the URL names(like index, detail,results) between different  apps
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #url(r'^notes/$', views.notes, name='notes'),

    url(r'^signup/$',  views.SignUpView.as_view(), name='signup'),
    url(r'^signin/$',  views.SignInView.as_view(), name='signin'),
    url(r'^signout/$', views.SignOutView.as_view(), name='signout'),

    url(r'^reset/$',   views.ResetView.as_view(), name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
                       views.ResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),

    #url(r'^signup/$', 'authentication.views.signup', name='signup'),
    #url(r'^signin/$', 'authentication.views.signin', name='signin'),
    #url(r'^signout/$', 'authentication.views.signout', name='signout'),

    #url(r'^reset/$', 'authentication.views.reset', name='reset'),
    #url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'authentication.views.reset_confirm', name='password_reset_confirm'),
    #url(r'^success/$', 'authentication.views.success', name='success'),
]
