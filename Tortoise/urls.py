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
    url(r'^pages/members', views.DeveloperView.as_view(), name = 'members'),
    path("",views.IndexView.as_view()),
    path('verification/',views.VerificationView.as_view()),
    url(r'^home', views.IndexView.as_view() ,name='home'),
    re_path(r'^pages/events/(?P<id>[0-9]{1,3})' , views.EventView.as_view()),
    url(r'^pages/events/',views.EventView.as_view() , name = 'events'),
    url(r'^pages/contact', contact.contact,name='contact'),
    re_path(r'^pages/projects/(?P<id>[0-9]{1,3})' , views.ProjectView.as_view()),
    url(r'^pages/projects/', views.ProjectView.as_view(),name='projects'),
    url(r'^pages/credits', views.TemplateView.as_view(template_name = 'credits.html'),name='credits'),
    url(r'^pages/privacy', views.TemplateView.as_view(template_name = 'privacy.html'),name='privacy'),
    url(r'^pages/rules', views.TemplateView.as_view(template_name = 'rules.html'),name='rules'),

]
    


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
