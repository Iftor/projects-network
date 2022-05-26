from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Project
from .serializers import ProjectSerializer


class CommunityProjectListView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        print(self.request.user)
        queryset = Project.objects.all()
        community_id = self.kwargs.get('community_id')
        return queryset.filter(community_id=community_id)


class ProjectDetailView(RetrieveAPIView):
    serializer_class = ProjectSerializer

    def get_object(self):
        project_id = self.kwargs.get('project_id')
        return Project.objects.get(id=project_id)
  