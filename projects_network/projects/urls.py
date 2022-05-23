from django.urls import path

from .views import CommunityProjectListView

urlpatterns = [
    path('communities/<int:community_id>', CommunityProjectListView.as_view(), name='community_project')
]