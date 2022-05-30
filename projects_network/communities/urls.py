from django.urls import path, include
from rest_framework import routers
from .views import CommunityViewSet, JoinCommunityView, LeaveCommunityView

router = routers.SimpleRouter()
router.register(r'', CommunityViewSet, basename='communities')

urlpatterns = [
    path('', include(router.urls)),
    path('join-community/<int:community_id>', JoinCommunityView.as_view(), name='join_community'),
    path('leave-community/<int:community_id>', LeaveCommunityView.as_view(), name='leave_community'),
]
