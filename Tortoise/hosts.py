from django.conf import settings
from django.contrib import admin
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'Tortoise.urls', name='www'),
    host(r'api', 'userdata.urls', name='api'),
    host(r'admin', 'admin.site.urls', name='admin'),

)