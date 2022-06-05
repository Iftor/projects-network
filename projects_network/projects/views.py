from django.utils import timezone
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Status, StatusConst
from session_authentication.session_authenticated import CsrfExemptSessionAuthentication
from .models import Project, Task
from .serializers import ProjectSerializer, CreateProjectSerializer, CreateTaskSerializer, TasksListSerializer


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


class CreateTaskView(CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = CreateTaskSerializer

    def perform_create(self, serializer):
        user = self.request.user
        project_id = self.kwargs.get('project_id')
        serializer.save(
            project_id=project_id,
            creator=user,
            status=Status.objects.get(name=StatusConst.IN_PROCESS)
        )


class TasksListView(ListAPIView):
    serializer_class = TasksListSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        tasks = Task.objects.filter(project_id=project_id, status__name=StatusConst.IN_PROCESS)
        return tasks


class CompleteTaskView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def put(self, request, task_id):
        try:
            user = request.user
            task = Task.objects.get(id=task_id)
            task.executor = user
            task.end_date = timezone.now()
            task.status = Status.objects.get(name=StatusConst.DONE)
            task.save()
            return Response('success')
        except Exception as err:
            print(err)
            return Response(
                {"non_field_errors": ["error"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
