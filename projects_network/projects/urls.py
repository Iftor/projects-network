from django.urls import path
from .views import CommunityProjectListView, ProjectDetailView

urlpatterns = [
    path('communities/<int:community_id>', CommunityProjectListView.as_view(), name='community_projects'),
    path('communities/<int:community_id>/<int:project_id>', ProjectDetailView.as_view(), name='project')
]
