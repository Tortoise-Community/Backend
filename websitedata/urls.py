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

from django.urls import path, re_path
from django.conf.urls import url
from .views import (IndexView, VerificationView, ProjectView, EventView,
                    DeveloperView, ContactView, TemplateView, VerificationHandlerView)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', IndexView.as_view(), name='home'),
    path('verification/', VerificationView.as_view()),

    re_path(r'^pages/projects/(?P<item_no>[0-9]{1,3})', ProjectView.as_view()),
    re_path(r'^pages/events/(?P<item_no>[0-9]{1,3})', EventView.as_view()),

    url(r'^pages/projects/', ProjectView.as_view(), name='projects'),
    url(r'^pages/members', DeveloperView.as_view(), name='members'),
    url(r'^pages/events/', EventView.as_view(), name='events'),
    url(r'^pages/contact', ContactView.as_view(), name='contact'),

    url(r'^pages/credits', TemplateView.as_view(template_name='credits.html'), name='credits'),
    url(r'^pages/privacy', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    url(r'^pages/rules', TemplateView.as_view(template_name='rules.html'), name='rules'),
    url(r'^verification/handlers/', VerificationHandlerView.as_view()),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
