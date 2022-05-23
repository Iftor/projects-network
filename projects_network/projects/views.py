from rest_framework.generics import ListAPIView
from .models import Project
from .serializers import ProjectSerializer


class CommunityProjectListView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        print(self.kwargs.get('community_id'))
        queryset = Project.objects.all()
        community_id = self.kwargs.get('community_id')
        return queryset.filter(community_id=community_id)
