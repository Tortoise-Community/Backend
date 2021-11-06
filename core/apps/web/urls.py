# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from .views import (
    ProjectView, EventView
)
from core.apps.ide.views import PasteView

urlpatterns = [
    path('projects/', ProjectView.as_view(), name='projects'),
    path('events/', EventView.as_view(), name='event'),
    path('projects/<str:slug>', ProjectView.as_view(), name='project_item'),
    path('events/<str:slug>', EventView.as_view(), name='event_item'),
    path('paste/', PasteView.as_view(), name='paste'),
    path('paste/<str:slug>', PasteView.as_view(), name='paste_item'),
]
