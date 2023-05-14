from rest_framework import serializers
from .models import Project, Hashtag
from accounts.serializers import UserSerializer

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = [
            'id', 'name', 'created_at'
        ]

class ProjectSerializer(serializers.ModelSerializer):
    user =  UserSerializer()
    hashtags = HashtagSerializer(many=True)
    class Meta:
        model = Project
        fields = [
            'id', 'user', 'name',
            'slug', 'description', 'hashtags',
            'created_at'
        ]


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'name', 'user', 'hashtags',
            'slug', 'description',
            'created_at'
        ]

    
    def to_representation(self, instance):
        rep = super(ProjectCreateSerializer, self).to_representation(instance)
        rep['user'] = UserSerializer(instance.user).data
        rep["hashtags"] = HashtagSerializer(instance.hashtags.all(), many=True).data
        return rep
