from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from session_authentication.session_authenticated import CsrfExemptSessionAuthentication
from .models import Project
from .serializers import ProjectSerializer, CreateProjectSerializer


class CommunityProjectListView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        community_id = self.kwargs.get('community_id')
        return queryset.filter(community_id=community_id)


class ProjectDetailView(RetrieveAPIView):
    serializer_class = ProjectSerializer

    def get_object(self):
        project_id = self.kwargs.get('project_id')
        return Project.objects.get(id=project_id)


class CreateProjectView(CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = CreateProjectSerializer

    def perform_create(self, serializer):
        community_id = self.kwargs.get('community_id')
        serializer.save(community_id=community_id)
