from django.urls import path,include,re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('members',views.MemberView)

urlpatterns = [
path('bot/', include(router.urls)),
#path('',views.api),
path('private/auth/', include('rest_framework.urls')),
path('private/members/',views.members),
path('private/members/edit/<int:id>/',views.members_edit),
path('private/projects/',views.projects),
path('private/projects/edit/<int:pk>/',views.projects_edit),
path('private/verify-confirmation/<int:id>/',views.is_verified),
path('private/top-members/',views.get_top_members),
path('private/members/<int:id>/roles/',views.get_member_roles),
path('private/rules/',views.get_rules),
#path('private/ping/',views.ping)
]