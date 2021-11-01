from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'www', 'web.urls', name='www'),
    host(r'api', 'api.urls', name='api'),
    host(r'staff', 'core.urls', name='staff'),
    host(r'dash', 'dash.urls', name='dashboard'),
)
