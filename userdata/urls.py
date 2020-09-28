from django.urls import path, include
from rest_framework import routers
from .views import (
    UserDataView, SuggestionDataView, MemberDataView, GuildDataView,
    ProjectStatsView, RulesDataView
)

router = routers.DefaultRouter()


urlpatterns = [
    path('private/bot/', include(router.urls)),
    path('private/auth/', include('rest_framework.urls')),

    path('private/suggestions/<int:guild_id>/', SuggestionDataView.as_view()),
    path('private/suggestions/item/<int:item_id>/', SuggestionDataView.as_view()),

    path('private/rules/<int:guild_id>/', RulesDataView.as_view()),
    path('private/guild/', GuildDataView.as_view()),
    path('private/guild/<int:guild_id>/', GuildDataView.as_view()),

    path('private/projects/', ProjectStatsView.as_view()),
    path('private/projects/<int:item_id>/', ProjectStatsView.as_view()),

    path('private/members/', MemberDataView.as_view()),
    path('private/members/<int:user_id>/<int:guild_id>/', MemberDataView.as_view()),
    path('private/user/<int:user_id>/', UserDataView.as_view()),
    path('private/user/', UserDataView.as_view()),
]
