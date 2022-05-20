from django.urls import path, include
from rest_framework import routers
from .views import CommunityViewSet


router = routers.SimpleRouter()
router.register(r'', CommunityViewSet, basename='communities')

urlpatterns = [
    path('', include(router.urls)),
]