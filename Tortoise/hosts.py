from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'www', 'websitedata.urls', name='www'),
    host(r'api', 'userdata.urls', name='api'),
    host(r'staff', 'Tortoise.admin_urls', name='staff'),
)
