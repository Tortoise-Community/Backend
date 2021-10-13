from django.conf import settings
from django.conf.urls import url
from django.urls import path, re_path
from django.conf.urls.static import static

from .views import (
    IndexView, VerificationView, ProjectView, EventView,
    DeveloperView, ContactView, TemplateView, VerificationHandlerView
)


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
