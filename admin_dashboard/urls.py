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
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginView, GuildPanelView, ServerView, BotView, logout_request, RegisterView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    # path('', LoginView.as_view(), name='login'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^guild/<int:guild_id>/', GuildPanelView.as_view(), name='panel'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    path('server/<str:template_name>', ServerView.as_view(), name='server'),
    path('bot/<str:template_name>', BotView.as_view(), name='server'),
]
