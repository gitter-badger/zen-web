from django.conf.urls import patterns, url

urlpatterns = patterns('mysite.apps.sessions.login.views',
    url(r'^$', 'login'),
    url(r'^submit/?$', 'login_submit'),
)
