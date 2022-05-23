from rest_framework import viewsets
from .models import Community
from .serializers import CommunitySerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
