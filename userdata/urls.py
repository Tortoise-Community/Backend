from django.urls import path, include
from rest_framework import routers
from .serializers import TopMemberSerializer, MemberMetaSerializer, MemberModSerializer
from .views import (
    DynamicMemberView, SuggestionDataView, MemberDataView, ServerMetaView,
    DeveloperDataView, ProjectStatsView, RulesDataView
)

router = routers.DefaultRouter()


urlpatterns = [
    path('private/bot/', include(router.urls)),
    path('private/auth/', include('rest_framework.urls')),

    path('private/suggestions/', SuggestionDataView.as_view()),
    path('private/suggestions/<int:item_id>/', SuggestionDataView.as_view()),

    path('private/rules/', RulesDataView.as_view()),
    path('private/server/meta/<int:item_id>/', ServerMetaView.as_view()),

    path('private/developers/', DeveloperDataView.as_view()),
    path('private/developers/<int:item_id>/', DeveloperDataView.as_view()),

    path('private/projects/', ProjectStatsView.as_view()),
    path('private/projects/<int:item_id>/', ProjectStatsView.as_view()),

    path('private/members/', MemberDataView.as_view()),
    path('private/members/<int:item_id>/', MemberDataView.as_view()),
    path('private/members/top/', DynamicMemberView.as_view(serializers=TopMemberSerializer)),
    path('private/members/meta/<int:item_id>/', DynamicMemberView.as_view(serializers=MemberMetaSerializer)),
    path('private/members/moderation/<int:item_id>/', DynamicMemberView.as_view(serializers=MemberModSerializer)),
]
