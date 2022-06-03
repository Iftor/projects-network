from django.urls import path
from .views import CommunityProjectListView, ProjectDetailView, CreateProjectView

urlpatterns = [
    path('communities/<int:community_id>', CommunityProjectListView.as_view(), name='community_projects'),
    path('communities/<int:community_id>/create-project', CreateProjectView.as_view(), name='create-project'),
    path('communities/<int:community_id>/<int:project_id>', ProjectDetailView.as_view(), name='project'),
]

