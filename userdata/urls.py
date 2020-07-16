from django.urls import path,include,re_path
from . import views
from rest_framework import routers
from .serializers import *
from . views import DynamicMemberView, SuggestionDataView

router = routers.DefaultRouter()
# router.register('members',views.MemberView)


urlpatterns = [
    # path('', views.api),
    # path('private/ping/', views.ping),
    # path('private/bot/', include(router.urls)),
    path('private/auth/', include('rest_framework.urls')),

    # Suggestion System
    path('private/suggestions/', SuggestionDataView.as_view()),
    path('private/suggestions/<int:item_id>/', SuggestionDataView.as_view()),

    # Server Meta
    path('private/rules/', views.RulesDataView.as_view()),
    path('private/server/meta/<int:id>/', views.ServerMetaView.as_view()),

    # Perks System
    path('private/developers/', views.DeveloperDataView.as_view()),
    path('private/developers/<int:item_id>/', views.DeveloperDataView.as_view()),

    # Project Stats
    path('private/projects/', views.ProjectStatsView.as_view()),
    path('private/projects/<int:item_id>/', views.ProjectStatsView.as_view()),

    # Member Data
    path('private/members/', views.MembedDataView.as_view()),
    path('private/members/<int:item_id>/', views.MembedDataView.as_view()),
    path('private/members/top/', views.DynamicMemberView.as_view(serializers=TopMemberSerializer)),
    path('private/members/meta/<int:item_id>/', DynamicMemberView.as_view(serializers=MemberMetaSerializer)),
    path('private/members/moderation/<int:item_id>/', DynamicMemberView.as_view(serializers=MemberModSerializer)),
]
