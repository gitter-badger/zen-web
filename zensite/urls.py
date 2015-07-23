#
# Licensed Materials - Property of esse.io
# 
# (C) Copyright esse.io. 2015 All Rights Reserved
#
# Author: Bryan HUANG (bryan@esse.io)
#
#

"""zensite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

js_info_dict = {
    'packages': ('zensite',),
}

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'zensite.apps.dashboard.views.display_dashboard'),
    url(r'^dashboard/?', include('zensite.apps.dashboard.urls')),
    url(r'^login/?', include('zensite.apps.sessions.login.urls')),
    url(r'^register/?', include('zensite.apps.sessions.register.urls')),
    url(r'^el/?', include('zensite.apps.el.urls')),
]

#TODO: search apps folder find all urls.py and append to urlpatterns

