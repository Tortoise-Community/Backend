from django.db import models
from django.contrib.auth import settings
from django.shortcuts import get_object_or_404
from django.contrib.postgres.fields import ArrayField

from utils.misc import empty_array


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32, default="")
    avatar = models.URLField(blank=True, default="https://cdn.discordapp.com/embed/avatars/4.png")
    tag = models.CharField(max_length=6, default=0)
    email = models.CharField(max_length=50, default="", blank=True)
    verified = models.BooleanField(default=False)
    perks = models.IntegerField(default=0)

    class Meta:
        unique_together = (('name', 'tag'),)


class Guild(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    event_submission = models.BooleanField(default=False)
    bug_report = models.BooleanField(default=False)
    mod_mail = models.BooleanField(default=False)
    suggestions = models.BooleanField(default=False)
    suggestion_message_id = models.BigIntegerField(default=0, blank=True)
    suggestion_channel_id = models.BigIntegerField(default=0, blank=True)
    verification_channel_id = models.BigIntegerField(default=0, blank=True)
    rules_channel_id = models.BigIntegerField(default=0, blank=True)
    roles_channel_id = models.BigIntegerField(default=0, blank=True)
    bot_log_channel_id = models.BigIntegerField(default=0, blank=True)
    member_log_channel_id = models.BigIntegerField(default=0, blank=True)
    update_log_channel_id = models.BigIntegerField(default=0, blank=True)
    deterrence_log_channel_id = models.BigIntegerField(default=0, blank=True)

    @classmethod
    def get_id_list(cls):
        return [obj.id for obj in cls.objects.all()]


class Role(models.Model):
    id = models.BigIntegerField(primary_key=True)
    number = models.IntegerField()
    emoji_id = models.BigIntegerField(default=0)
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="roles")

    class Meta:
        unique_together = (('id', 'guild'), ('id', 'emoji_id'), ('number', 'guild'))


class Member(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role, blank=True)
    mod_mail = models.BooleanField(default=False)
    member = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True)
    leave_date = models.DateTimeField(blank=True, default=None)

    class Meta:
        unique_together = (('user', 'guild'),)

    @classmethod
    def get_instance(cls, member_id: int, guild_id: int):
        return get_object_or_404(cls, user__id=member_id, guild_id=guild_id)


class Strike(models.Model):
    ads = models.IntegerField(default=0)
    spam = models.IntegerField(default=0)
    bad_words = models.IntegerField(default=0)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="strikes")


class MemberWarning(models.Model):
    reason = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    moderator: Member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name="issued_warnings")
    member: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="warned_member")


class Infractions(models.Model):
    class InfractionsChoice(models.TextChoices):
        SHORT_MUTE = "SM", "Short Mute"
        LONG_TEMPORARY_MUTE = "LM", "Long Temporary Mute"
        KICK = "SK", "Kick"
        SHORT_TEMPORARY_BAN = "SB", "Short Temporary Ban"
        LONG_TEMPORARY_BAN = "LB", "Long Temporary Ban"
        PERMANENT_BAN = "PB", "Permanent Ban"

    member: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="infractions")
    warning: MemberWarning = models.ForeignKey(MemberWarning, on_delete=models.CASCADE, related_name="infraction")
    type = models.CharField(max_length=30, choices=InfractionsChoice.choices, default=InfractionsChoice.SHORT_MUTE)
    revoke_date = models.DateTimeField(default=None)


class Projects(models.Model):
    class StatusCSS(models.TextChoices):
        CATA_RED = "cata red", "Started"
        CATA_GREEN = "cata green", "Upcoming"
        CATA_YELLOW = "cata yellow", "Completed"
        CATA_PURPLE = "cata purple", "Refactoring"

    name = models.CharField(max_length=15)
    coverimage = models.ImageField(upload_to='img/bgimgs') # noqa
    rating = models.FloatField(default=0.0, blank=True)
    label = models.CharField(max_length=100)
    brief = models.TextField()
    status = models.CharField(max_length=16, choices=StatusCSS.choices, default=StatusCSS.CATA_PURPLE)
    github = models.URLField(blank=True)
    invite = models.URLField(blank=True)
    commits = models.IntegerField(blank=True, default=0)
    stars = models.IntegerField(blank=True, default=0)
    forks = models.IntegerField(blank=True, default=0)
    contributors = models.IntegerField(blank=True, default=0)


class Rules(models.Model):
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="guild_rule")
    number = models.IntegerField(blank=True)
    name = models.CharField(max_length=20, default="Rule name")
    statement = models.TextField(blank=True)
    alias = ArrayField(models.CharField(max_length=20), default=empty_array)

    class Meta:
        unique_together = (('number', 'guild'),)


class Suggestions(models.Model):
    class SuggestionStatus(models.TextChoices):
        UNDER_REVIEW = "R", "Under Review"
        APPROVED = "A", "Approved"
        DENIED = "D", "Denied"

    message_id = models.BigIntegerField(primary_key=True)
    author: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suggestion_author')
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="suggestion_guild")
    brief = models.CharField(max_length=2000)
    status = models.CharField(max_length=20, choices=SuggestionStatus.choices, default=SuggestionStatus.UNDER_REVIEW)
    reason = models.CharField(max_length=2000, default="", blank=True)
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)


class Admins(models.Model):
    authuser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    guild: Guild = models.ManyToManyField(Guild)

    def get_admin_guilds(self):
        return [guild.id for guild in self.guild.all()]

    def get_admin_guild_names(self):
        return {guild.id: guild.name for guild in self.guild.all()}
