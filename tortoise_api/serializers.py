from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import User, Member, Guild, Suggestions, Rules, Projects, Role, MemberWarning, Strike, Infractions


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("email",)
        extra_kwargs = {
            'id': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class GuildDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = "__all__"
        extra_kwargs = {
            'id': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ('number', 'name', 'alias', 'statement')


class ProjectStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('pk', 'stars', 'forks', 'commits', 'contributors', 'github')


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = '__all__'


class GuildMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        exclude = ("id", "name")


class MemberDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = ("user", "guild")


class SuggestionPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = ('status', 'reason')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberWarning
        exclude = ("id", "date")


class StrikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strike
        exclude = ("id",)

    def update(self, instance, validated_data):
        instance = Strike.objects.update_or_create(**validated_data)
        return instance


class InfractionSerializer(serializers.ModelSerializer):
    warning = WarningSerializer()

    class Meta:
        model = Infractions
        exclude = ("member",)


class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("name", "email", "tag", "id")
