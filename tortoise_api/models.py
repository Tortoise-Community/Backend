from django.db import models
from django.contrib.auth import settings
from django.shortcuts import get_object_or_404
from django.contrib.postgres.fields import ArrayField

from utils.misc import empty_array, DiscordIDField


class User(models.Model):
    id = DiscordIDField(primary_key=True)
    name = models.CharField(max_length=32)
    tag = models.CharField(max_length=6)
    avatar = models.URLField(max_length=150, blank=True, default="https://cdn.discordapp.com/embed/avatars/4.png")
    email = models.CharField(max_length=50, default="", blank=True)  # TODO email validator
    verified = models.BooleanField(default=False)
    perks = models.PositiveIntegerField(default=0)


class Guild(models.Model):
    id = DiscordIDField(primary_key=True)
    name = models.CharField(max_length=100)
    event_submission = models.BooleanField(default=False)
    bug_report = models.BooleanField(default=False)
    mod_mail = models.BooleanField(default=False)
    suggestions = models.BooleanField(default=False)
    suggestion_message_id = DiscordIDField()
    suggestion_channel_id = DiscordIDField()
    verification_channel_id = DiscordIDField()
    rules_channel_id = DiscordIDField()
    roles_channel_id = DiscordIDField()
    bot_log_channel_id = DiscordIDField()
    member_log_channel_id = DiscordIDField()
    update_log_channel_id = DiscordIDField()
    deterrence_log_channel_id = DiscordIDField()

    @classmethod
    def get_id_list(cls):
        # TODO unneeded
        return [obj.id for obj in cls.objects.all()]


class Role(models.Model):
    id = DiscordIDField(primary_key=True)
    number = models.IntegerField(help_text="Please describe this ffs I keep forgetting what it is.")  # TODO
    emoji_id = DiscordIDField()
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="roles")

    class Meta:
        unique_together = (('id', 'guild'), ('id', 'emoji_id'), ('number', 'guild'))


class Member(models.Model):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="members")
    roles = models.ManyToManyField(Role, blank=True)
    mod_mail = models.BooleanField(default=False)
    member = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True)
    leave_date = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        unique_together = (('user', 'guild'),)

    @classmethod
    def get_instance(cls, member_id: int, guild_id: int):
        return get_object_or_404(cls, user__id=member_id, guild_id=guild_id)


class Strike(models.Model):
    ads = models.PositiveSmallIntegerField(default=0)
    spam = models.PositiveSmallIntegerField(default=0)
    bad_words = models.PositiveSmallIntegerField(default=0)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="strikes")


class MemberWarning(models.Model):
    reason = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    moderator: Member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name="issued_warnings")
    member: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="warnings")


class Infractions(models.Model):
    class InfractionsChoice(models.TextChoices):
        SHORT_MUTE = "SM", "Short Mute"
        LONG_TEMPORARY_MUTE = "LM", "Long Temporary Mute"
        KICK = "SK", "Kick"
        SHORT_TEMPORARY_BAN = "SB", "Short Temporary Ban"
        LONG_TEMPORARY_BAN = "LB", "Long Temporary Ban"
        PERMANENT_BAN = "PB", "Permanent Ban"

    member: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="infractions")
    type = models.CharField(max_length=30, choices=InfractionsChoice.choices, default=InfractionsChoice.SHORT_MUTE)
    revoke_date = models.DateTimeField(null=True, blank=True, default=None)


class Rules(models.Model):
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="rules")
    number = models.IntegerField(blank=True)
    name = models.CharField(max_length=20)
    statement = models.TextField()
    alias = ArrayField(models.CharField(max_length=20), default=empty_array)

    class Meta:
        unique_together = (('number', 'guild'),)


class Suggestions(models.Model):
    class SuggestionStatus(models.TextChoices):
        UNDER_REVIEW = "R", "Under Review"
        APPROVED = "A", "Approved"
        DENIED = "D", "Denied"

    message_id = DiscordIDField(primary_key=True)
    author: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="suggestions")
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="suggestion")
    brief = models.CharField(max_length=2000)
    status = models.CharField(max_length=20, choices=SuggestionStatus.choices, default=SuggestionStatus.UNDER_REVIEW)
    reason = models.CharField(max_length=2000, default="No reason specified.", blank=True)
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)


class Admins(models.Model):
    auth_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    guild: Guild = models.ManyToManyField(Guild)

    def get_admin_guilds(self):
        # TODO why are guilds even important? If it's needed then remove user and guild and just have
        #  foreign key pointing to member
        return [guild.id for guild in self.guild.all()]

    def get_admin_guild_names(self):
        # TODO read above todo
        return {guild.id: guild.name for guild in self.guild.all()}
