from rest_framework import serializers
from .models import Members
from . import views

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Members
        fields = ['user_id','guild_id']


class AllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields ='__all__'     

