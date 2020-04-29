from rest_framework import serializers
from .models import *
from . import views

class MemberRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Members
        fields = ['roles']


class AllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        exclude = ('email',) 

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
        fields = ['user_id','name','tag','perks']

class MemberPostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Members
        fields = ['user_id','guild_id','join_date','member','name','tag']

class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ['number','alias','statement']      
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerUtils
        fields = ['bot_status']    
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerUtils
        fields = ['Github_Microservice','Status_Microservice','Tortoise_BOT','Tortoise_BOT2','Website','Sockets','API_Gateway']       
      
class DeveloperSerializer(serializers.ModelSerializer):
	class Meta:
		model = Developers
		fields = '__all__'   

class SuggestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Suggestion
		fields = '__all__'   

class SuggestionPutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Developers
		fields = ['status','reason']   
