from django.urls import path,include,re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('members',views.MemberView)

urlpatterns = [
path('bot/', include(router.urls)),
path('',views.api),
path('api-auth/', include('rest_framework.urls')),
path('members',views.members),
path('members/edit/<int:id>',views.members_edit),
]