from rest_framework import serializers
from users.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100, style={"placeholder": "username", "autofocus": True}
    )
    password = serializers.CharField(
        max_length=100, style={"input_type": "password", "placeholder": "Password"}
    )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
