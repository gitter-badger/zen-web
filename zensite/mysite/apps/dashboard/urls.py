from django.conf.urls import patterns, url

urlpatterns = patterns('mysite.apps.dashboard.views',
    url(r'^$', 'display_dashboard'),
    url(r'^dashboard/', 'display_dashboard'),
)
