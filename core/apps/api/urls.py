from rest_framework import routers
from django.urls import path, include

from .views import (
    UserDataView, SuggestionDataView, MemberDataView, GuildDataView,
    RulesDataView, RolesDataView, InfractionDataView,
    MemberWarningView, StrikeDataView
)


router = routers.DefaultRouter()


urlpatterns = [
    path('private/bot/', include(router.urls)),
    path('private/auth/', include('rest_framework.urls')),

    path('private/suggestions/', SuggestionDataView.as_view()),
    path('private/suggestions/<int:guild_id>/', SuggestionDataView.as_view()),
    path('private/suggestions/item/<int:item_id>/', SuggestionDataView.as_view()),

    path('private/rules/<int:guild_id>/', RulesDataView.as_view()),
    path('private/guild/', GuildDataView.as_view()),
    path('private/guild/<int:guild_id>/', GuildDataView.as_view()),


    path('private/members/', MemberDataView.as_view()),
    path('private/members/<int:guild_id>/', MemberDataView.as_view()),
    path('private/members/<int:guild_id>/<int:user_id>/', MemberDataView.as_view()),

    path('private/user/<int:user_id>/', UserDataView.as_view()),
    path('private/user/', UserDataView.as_view()),
    path('private/user/<int:user_id>/strikes/', StrikeDataView.as_view()),

    path('private/roles/<int:guild_id>/', RolesDataView.as_view()),
    path('private/roles/', RolesDataView.as_view()),

    path('private/strikes/', StrikeDataView.as_view()),

    path('private/warnings/', MemberWarningView.as_view()),
    path('private/warnings/<int:guild_id>/<int:user_id>/', MemberWarningView.as_view()),
    path('private/warnings/<int:guild_id>/', MemberWarningView.as_view()),

    path('private/infractions/', InfractionDataView.as_view()),
    path('private/infractions/<int:guild_id>/', InfractionDataView.as_view()),
    path('private/infractions/<int:guild_id>/<int:user_id>/', InfractionDataView.as_view()),
]
