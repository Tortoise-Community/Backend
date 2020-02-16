from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'Tortoise.urls', name='www'),
    #host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'api', 'userdata.urls', name='api'),
)