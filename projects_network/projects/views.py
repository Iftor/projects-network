from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class JoinProjectView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, project_id):
        try:
            user = request.user
            project = Project.objects.get(id=project_id)
            project.participants.add(user)

            return Response('success')
        except:
            return Response(
                {"non_field_errors": ["error"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
