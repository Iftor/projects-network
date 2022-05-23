from rest_framework import viewsets
from rest_framework.response import Response

from .models import Community
from .serializers import CommunitySerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def perform_create(self, serializer):
        serializer.save(creator_id=1)
