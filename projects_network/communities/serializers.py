
from rest_framework import serializers
from .models import Community


class CommunitySerializer(serializers.ModelSerializer):
    auth_user_participation = serializers.SerializerMethodField()
    auth_user_is_creator = serializers.SerializerMethodField()

    class Meta:
        model = Community
        exclude = ['creating_date']

    def get_auth_user_participation(self, obj):
        user = self.context['request'].user
        return user in obj.participants.all()

    def get_auth_user_is_creator(self, obj):
        user = self.context['request'].user
        return user == obj.creator
