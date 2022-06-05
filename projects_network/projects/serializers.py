from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Project, Task


class ProjectSerializer(ModelSerializer):
    auth_user_participation = serializers.SerializerMethodField()
    auth_user_is_community_creator = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_auth_user_participation(self, obj):
        user = self.context['request'].user
        return user in obj.participants.all()

    def get_auth_user_is_community_creator(self, obj):
        user = self.context['request'].user
        return user == obj.community.creator


class CreateProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', 'description', 'deadline')


class CreateTaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline')


class TasksListSerializer(ModelSerializer):
    creator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'deadline', 'creator')
