from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'web', 'web.urls', name='web'),
    # host(r'api', 'api.urls', name='api'),
    host(r'staff', 'core.urls', name='staff'),
    # host(r'dash', 'dash.urls', name='dashboard'),
)
