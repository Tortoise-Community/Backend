from django.urls import path,include,re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('members',views.MemberView)

urlpatterns = [
#path('',views.api),
path('private/ping/',views.ping),
path('private/bot/',include(router.urls)),
path('private/rules/',views.get_rules),
path('private/members/',views.members),
path('private/projects/',views.projects),
path('private/services/<int:id>/',views.get_services),
path('private/bot/status/<int:id>/',views.manage_bot_status),
path('private/top-members/',views.get_top_members),
path('private/developers/edit/<int:id>/',views.put_top_developers),
path('private/auth/', include('rest_framework.urls')),
path('private/members/edit/<int:id>/',views.members_edit),
path('private/projects/edit/<int:pk>/',views.projects_edit),
path('private/members/<int:id>/roles/',views.get_member_roles),
path('private/verify-confirmation/<int:id>/',views.is_verified),
path('private/developers/',views.developers),
path('private/suggestions/',views.suggestions),
path('private/suggestions/<ind:id>/',views.suggestions_edit)

]
