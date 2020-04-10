"""Tortoise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url
from . import views,contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^pages/members', views.members, name = 'members'),
    path("",views.index),
    path('verification/',views.verified),
    url(r'^home', views.index ,name='home'),
    re_path(r'^pages/events/(?P<item_name>[0-9]{1,3})' , views.get_event),
    url(r'^pages/events/',views.events , name = 'events'),
    url(r'^pages/contact', contact.contact,name='contact'),
    re_path(r'^pages/projects/(?P<item_name>[0-9]{1,3})' , views.get_project),
    url(r'^pages/projects', views.projects,name='projects'),
    url(r'^pages/credits', views.credits,name='credits'),
    url(r'^pages/privacy', views.privacypolicy,name='privacy'),
    url(r'^pages/rules', views.rules,name='rules'),

]
    


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
