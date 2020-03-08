from rest_framework import serializers
from .models import Members,Projects
from . import views

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Members
        fields = ['user_id','guild_id']


class AllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields ='__all__'     

class GithubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['pk','github']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['commits','stars','forks','collaborators']        