
from rest_framework import serializers
from .models import Community


class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        exclude = ['creating_date']
