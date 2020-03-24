from rest_framework import serializers
from .models import Members,Projects
from . import views

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Members
        fields = ['user_id','guild_id','join_date']


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
        fields = ['commits','stars','forks','contributors']        

class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['verified']

class TopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['user_id']
