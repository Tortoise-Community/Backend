from rest_framework import serializers
from .models import User, Member, Guild, Suggestions, Rules, Projects
from django.contrib.auth.validators import UnicodeUsernameValidator

# REST API GENERIC MODEL SERIALIZERS


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'id': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class GuildDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        # fields = ('id', 'name')  # "__all__"
        exclude = ("suggestion_message_id",)
        extra_kwargs = {
            'id': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class MemberDataSerializer(serializers.ModelSerializer):
    user = UserDataSerializer()
    guild = GuildDataSerializer()

    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        print("Serializer activated")
        user_data = validated_data.pop("user")
        guild_data = validated_data.pop("guild")
        user, created = User.objects.get_or_create(**user_data)
        guild = Guild.objects.get(id=guild_data.get('id'))
        return Member.objects.create(user=user, guild=guild)


class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ('number', 'name', 'alias', 'statement')


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = '__all__'


class SuggestionPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = ('status', 'reason')


class MemberMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('join_date', 'leave_date', 'mod_mail', 'verified', 'member', 'roles')


class MemberModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('warnings', 'muted_until', 'strikes', 'perks')


class TopMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('user_id', 'name', 'tag', 'perks')


class ProjectStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('pk', 'stars', 'forks', 'commits', 'contributors', 'github')
