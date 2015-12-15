"""sbtc URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from sbtcapp import views
from sbtcapp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='sbtchome'),
    url(r'^weare',WeAre.as_view(), name='weare'),
    url(r'^ourteam',OurTeam.as_view(),  name='ourteam'),
    url(r'^meetamazing',MeetOur.as_view(),  name='meetamazing'),
    url(r'^clients',Clients.as_view(),  name='CorporateClients'),
    url(r'^contact',ContactUs.as_view(), name='ContactUs'),
    url(r'^projects',ProjectDone.as_view(), name='ProjectDone'),
    
]
