from django.urls import path
from django.conf.urls import url

from .views import (
    LoginView, GuildPanelView,
    logout_request, GuildRulesView,
    GuildRolesView, GuildInfractionView,
    GuildWarningsView, BotSecurityView, BotMusicView,
    BotLoggingView, BotUtilityView, BotFunView, BotOtherView)


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/rules', GuildRulesView.as_view(), name='guild_rules'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/roles', GuildRolesView.as_view(), name='guild_roles'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/infractions', GuildInfractionView.as_view(), name='guild_infractions'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/warnings', GuildWarningsView.as_view(), name='guild_warnings'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/bot-security', BotSecurityView.as_view(), name='bot_security'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/bot-logging', BotLoggingView.as_view(), name='bot_logging'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/bot-utility', BotUtilityView.as_view(), name='bot_utility'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/bot-music', BotMusicView.as_view(), name='bot_music'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/bot-other', BotOtherView.as_view(), name='bot_other'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/bot-fun', BotFunView.as_view(), name='bot_fun'),
    url(r'^guild/(?P<guild_id>[0-9]{18})/$', GuildPanelView.as_view(), name='guild'),
    url(r'^logout/', logout_request, name='logout'),
]
