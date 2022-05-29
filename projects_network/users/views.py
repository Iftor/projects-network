from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import LoginSerializer


class Login(GenericAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        if self.request.user.is_authenticated:
            raise ValidationError()
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get("username")
        password = serializer.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'username': username})
        else:
            return Response(
                {"non_field_errors": ["incorrect username or password"]},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            if self.request.user is not None:
                logout(request)
                return Response('success')
            else:
                return Response(
                    {"non_field_errors": ["error"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception:
            return Response(
                {"non_field_errors": ["error"]},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CheckAuthenticated(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            authenticated = request.user.is_authenticated
            if authenticated:
                return Response({
                    'authenticated': 'true',
                    'username': request.user.username
                })
            else:
                return Response({'authenticated': 'false'})
        except Exception:
            return Response(
                    {"non_field_errors": ["error"]},
                    status=status.HTTP_400_BAD_REQUEST,
            )
