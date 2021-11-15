from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'web', 'core.apps.web.urls', name='web'),
    host(r'api', 'core.apps.api.url_router', name='api'),
    host(r'staff', 'core.urls', name='staff'),
    # host(r'dash', 'dash.urls', name='dashboard'),
)
