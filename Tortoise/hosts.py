from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'Tortoise.urls', name='www'),
    host(r'(?!www).*', 'userdata.urls', name='api'),
)