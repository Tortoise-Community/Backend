from rest_framework import serializers
from .models import Members, ServerUtils, Suggestions, Rules, Projects, Developers

# REST API GENERIC MODEL SERIALIZERS


class MemberDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        exclude = ('email',)


class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ('number', 'alias', 'statement')


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = '__all__'


class SuggestionPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = ('status', 'reason')


class ServerMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerUtils
        fields = ('event_submission', 'mod_mail', 'bug_report',
                  'suggestions', 'suggestion_message_id', 'bot_status')


class MemberMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('join_date', 'leave_date', 'mod_mail', 'verified', 'member', 'roles')


class MemberModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('warnings', 'muted_until', 'strikes', 'perks')


class TopMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('user_id', 'name', 'tag', 'perks')


class ProjectStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('pk', 'stars', 'forks', 'commits', 'contributors', 'github')


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developers
        exclude = ('no',)
