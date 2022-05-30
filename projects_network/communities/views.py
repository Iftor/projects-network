from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from session_authentication.session_authenticated import CsrfExemptSessionAuthentication
from .models import Community
from .serializers import CommunitySerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(creator_id=1)


class JoinCommunityView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, community_id):
        try:
            user = request.user
            community = Community.objects.get(id=community_id)
            community.participants.add(user)

            return Response('success')
        except:
            return Response(
                {"non_field_errors": ["error"]},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LeaveCommunityView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, community_id):
        try:
            user = request.user
            community = Community.objects.get(id=community_id)
            community.participants.remove(user)

            return Response('success')
        except:
            return Response(
                {"non_field_errors": ["error"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
