from django.urls import path
from .views import CommunityProjectListView, ProjectDetailView, CreateProjectView, CreateTaskView, TasksListView, \
    JoinProjectView, CompleteTaskView

urlpatterns = [
    path('communities/<int:community_id>/project-list', CommunityProjectListView.as_view(), name='community_projects'),
    path('communities/<int:community_id>/create-project', CreateProjectView.as_view(), name='create-project'),
    path('<int:project_id>', ProjectDetailView.as_view(), name='project_detail'),
    path('<int:project_id>/join-project', JoinProjectView.as_view(), name='join_project'),
    path('<int:project_id>/create-task', CreateTaskView.as_view(), name='create_task'),
    path('<int:project_id>/tasks-list', TasksListView.as_view(), name='tasks_list'),
    path('<int:task_id>/complete-task', CompleteTaskView.as_view(), name='complete_task'),
]

