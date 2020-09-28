from rest_framework import serializers
from .models import User, Member, Guild, Suggestions, Rules, Projects, Role
from django.contrib.auth.validators import UnicodeUsernameValidator


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


class MemberSerializer(serializers.ModelSerializer):
    user = UserDataSerializer()
    guild = GuildDataSerializer()

    class Meta:
        model = Member
        exclude = ("id",)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        guild_data = validated_data.pop("guild")
        user, created = User.objects.get_or_create(**user_data)
        guild = Guild.objects.get(id=guild_data.get("id"))
        return Member.objects.create(user=user, guild=guild)


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

