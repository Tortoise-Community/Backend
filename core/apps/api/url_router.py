from django.urls import path, include

urlpatterns = [
    path('private/', include('core.apps.api.private.urls')),
]
