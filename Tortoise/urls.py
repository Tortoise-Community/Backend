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
    #path('admin/', admin.site.urls),
    url(r'^members/verify', views.verify ,name='verify'),
    url(r'^members', views.members, name = 'members'),
    path("",views.index),
    path('verified/',views.verified),
    url(r'^home', views.index ,name='home'),
    re_path(r'^events/(?P<item_name>[0-9]{1,3})' , views.get_event),
    url(r'^events/',views.events , name = 'events'),
    url(r'^contact', contact.contact,name='contact'),
    re_path(r'^projects/(?P<item_name>[0-9]{1,3})' , views.get_project),
    url(r'^projects', views.projects,name='projects'),
    url(r'^credits', views.credits,name='credits'),
    url(r'^announcements', views.announcements,name='announcements'),
    url(r'^privacy', views.privacy,name='privacy'),

]
    


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
