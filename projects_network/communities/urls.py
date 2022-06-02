from django.urls import path, include
from rest_framework import routers
from .views import CommunityViewSet, JoinCommunityView, LeaveCommunityView, CommunityParticipants

router = routers.SimpleRouter()
router.register(r'', CommunityViewSet, basename='communities')

urlpatterns = [
    path('join-community/<int:community_id>', JoinCommunityView.as_view(), name='join_community'),
    path('leave-community/<int:community_id>', LeaveCommunityView.as_view(), name='leave_community'),
    path('participants/<int:community_id>', CommunityParticipants.as_view(), name='participants'),
    path('', include(router.urls)),
]
