from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator

from .. import models


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ("email",)
        extra_kwargs = {
            'id': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class GuildOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuildOption
        exclude = ("id",)


class GuildChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuildChannel
        exclude = ("id",)


class GuildRolesSpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuildRolesSpecial
        exclude = ("id",)


class GuildDataSerializer(serializers.ModelSerializer):
    options = GuildOptionSerializer()
    channels = GuildChannelSerializer()
    roles_special = GuildRolesSpecialSerializer()

    class Meta:
        model = models.Guild
        fields = "__all__"
        extra_kwargs = {
            'id': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rule
        fields = ('number', 'name', 'alias', 'statement')


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Suggestion
        fields = '__all__'


class GuildMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guild
        exclude = ("id", "name")


class MemberDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        exclude = ("user", "guild")


class SuggestionPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Suggestion
        fields = ('status', 'reason')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"


class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MemberWarning
        exclude = ("id", "date")


class StrikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Strike
        exclude = ("id",)

    def update(self, instance, validated_data):
        instance = models.Strike.objects.update_or_create(**validated_data)
        return instance


class InfractionSerializer(serializers.ModelSerializer):
    warning = WarningSerializer()

    class Meta:
        model = models.Infraction
        exclude = ("member",)


class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ("name", "email", "tag", "id")
