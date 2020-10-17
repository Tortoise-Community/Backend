from django.urls import path
from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static
from .views import(
    LoginView, GuildPanelView,
    logout_request, GuildRulesView,
    GuildRolesView, GuildInfractionView,
    GuildWarningsView)



urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/rules', GuildRulesView.as_view(), name='guild_rules'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/roles', GuildRolesView.as_view(), name='guild_roles'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/infractions', GuildInfractionView.as_view(), name='guild_infractions'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/warnings', GuildWarningsView.as_view(), name='guild_warnings'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/', GuildPanelView.as_view(), name='guild'),
    url(r'^logout/', logout_request, name='logout'),
]
