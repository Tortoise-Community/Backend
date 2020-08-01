from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from utils.misc import status_css_class, empty_dict, empty_array, default_strikes


class Members(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    tag = models.CharField(max_length=6, blank=True, null=True)
    user_id = models.BigIntegerField(primary_key=True)
    guild_id = models.BigIntegerField()
    email = models.TextField(blank=True, null=True)
    perks = models.IntegerField(blank=True, null=True, default=0)
    join_date = models.DateTimeField(blank=True, null=True)
    leave_date = models.DateTimeField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True, default=False)
    strikes = JSONField(null=True, default=default_strikes)
    mod_mail = models.BooleanField(blank=True, null=True, default=False)
    warnings = ArrayField(models.CharField(max_length=300), null=True, default=empty_array, blank=True)
    roles = ArrayField(models.BigIntegerField(), null=True, default=empty_array, blank=True)
    muted_until = models.DateTimeField(blank=True, null=True)
    member = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        unique_together = (('user_id', 'guild_id'),)


class Projects(models.Model):

    name = models.CharField(max_length=15)
    coverimage = models.ImageField(upload_to='img/bgimgs') # noqa
    rating = models.FloatField(default=None, blank=True)
    label = models.CharField(max_length=100, default=None)
    brief = models.TextField(default=None)
    status = models.CharField(max_length=16, choices=status_css_class, default='Upcoming')
    github = models.URLField(blank=True)
    invite = models.URLField(blank=True)
    commits = models.IntegerField(blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    forks = models.IntegerField(blank=True, null=True)
    contributors = models.IntegerField(blank=True, null=True)


class Rules(models.Model):
    number = models.IntegerField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    alias = ArrayField(models.CharField(max_length=20), null=True, default=empty_array, blank=True)


class ServerUtils(models.Model):
    guild_id = models.BigIntegerField(primary_key=True)
    event_submission = models.BooleanField(null=True, default=False)
    bug_report = models.BooleanField(null=True, default=False)
    mod_mail = models.BooleanField(null=True, default=False)
    suggestions = models.BooleanField(null=True, default=False)
    suggestion_message_id = models.BigIntegerField(null=True, blank=True)
    bot_status = JSONField(null=True, default=empty_dict, blank=True)


class Developers(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    tag = models.CharField(max_length=6, blank=True, null=True)
    perks = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, default=None, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=35, default=None, blank=True, null=True)


class Suggestions(models.Model):
    message_id = models.BigIntegerField(primary_key=True)
    author_id = models.BigIntegerField()
    author_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    brief = models.TextField(default=None)
    status = models.CharField(max_length=20, default="Under Review")
    reason = models.TextField(default=None, null=True, blank=True)
    avatar = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True)
    date = models.DateTimeField(blank=True, null=True)
