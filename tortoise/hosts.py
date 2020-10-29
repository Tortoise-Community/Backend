from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'www', 'tortoise_web.urls', name='www'),
    host(r'api', 'tortoise_api.urls', name='api'),
    host(r'staff', 'tortoise.urls', name='staff'),
    host(r'dashboard', 'tortoise_dash.urls', name='dashboard'),
)
