from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    #reference= serializers.CharField(max_length=511)
    title = serializers.CharField(source='reference')
    link= serializers.URLField(max_length=511)
    explanation= serializers.CharField(max_length=5095)
    adddate= serializers.DateField(read_only=True)
    total_views=serializers.IntegerField(read_only=True)
    class Meta:
        model= Publication
        fields = [
            'title',
            'link',
            'explanation',
            'pk',
            'adddate',
            'total_views', 
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']