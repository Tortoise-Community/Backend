from django.db import models
from utils.misc import status_css_class, empty_array
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    avatar = models.URLField(blank=True, null=True)
    tag = models.CharField(max_length=6)
    email = models.CharField(max_length=50, null=True, blank=True)
    verified = models.BooleanField(default=False)
    perks = models.IntegerField(default=0)

    class Meta:
        unique_together = (('name', 'tag'),)


class Guild(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    event_submission = models.BooleanField(default=False)
    bug_report = models.BooleanField(default=False)
    mod_mail = models.BooleanField(default=False)
    suggestions = models.BooleanField(default=False)
    suggestion_message_id = models.BigIntegerField(default=0, null=True, blank=True)
    suggestion_channel_id = models.BigIntegerField(default=0, null=True, blank=True)
    verification_channel_id = models.BigIntegerField(default=0, null=True, blank=True)
    rules_channel_id = models.BigIntegerField(default=0, null=True, blank=True)
    roles_channel_id = models.BigIntegerField(default=0, null=True, blank=True)
    bot_log_channel_id = models.BigIntegerField(default=0, null=True, blank=True)
    member_log_channel_id = models.BigIntegerField(default=0, null=True, blank=True)
    update_log_channel_id = models.BigIntegerField(default=0, null=True, blank=True)
    deterrence_log_channel_id = models.BigIntegerField(default=0, null=True, blank=True)


class Role(models.Model):
    id = models.BigIntegerField(primary_key=True)
    emoji_id = models.BigIntegerField(default=0)
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="roles")

    class Meta:
        unique_together = (('id', 'guild'), ('id', 'emoji_id'))


class Member(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role, blank=True)
    mod_mail = models.BooleanField(default=False)
    member = models.BooleanField(default=False)
    muted_until = models.DateTimeField(blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    leave_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = (('user', 'guild'),)


class Strike(models.Model):
    ads = models.IntegerField(default=0)
    spam = models.IntegerField(default=0)
    bad_words = models.IntegerField(default=0)
    member: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="strikes")


class MemberWarning(models.Model):
    reason = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    moderator: Member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name="issued_warnings")
    member: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="warnings")


class Infractions(models.Model):
    INFRACTIONS = (("Short Mute", "SM"),
                   ("Long Temporary Mute", "LM"),
                   ("Kick", "SK"),
                   ("Short Temporary Ban", "SB"),
                   ("Long Temporary Ban", "LB"),
                   ("Permanent Ban", "PB")
                   )
    member: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="infractions")
    warning: MemberWarning = models.ForeignKey(MemberWarning, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=INFRACTIONS, default="SM")
    revoke_date = models.DateTimeField(null=True)


class Projects(models.Model):
    name = models.CharField(max_length=15)
    coverimage = models.ImageField(upload_to='img/bgimgs') # noqa
    rating = models.FloatField(default=None, blank=True)
    label = models.CharField(max_length=100)
    brief = models.TextField(default=None)
    status = models.CharField(max_length=16, choices=status_css_class, default='Upcoming')
    github = models.URLField(blank=True)
    invite = models.URLField(blank=True)
    commits = models.IntegerField(blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    forks = models.IntegerField(blank=True, null=True)
    contributors = models.IntegerField(blank=True, null=True)


class Rules(models.Model):
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="guild_rule")
    number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, null=True, default="Rule name")
    statement = models.TextField(blank=True, null=True)
    alias = ArrayField(models.CharField(max_length=20), default=empty_array)


class Suggestions(models.Model):
    STATUS = (("Under Review", "R"),
              ("Approved", "A"),
              ("Denied", "D")
              )
    message_id = models.BigIntegerField(primary_key=True)
    author: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='suggestion_author')
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="suggestion_guild")
    brief = models.CharField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS, default="R")
    reason = models.CharField(max_length=2000, default="", blank=True)
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)


class Admins(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    guild: Guild = models.ManyToManyField(Guild)
