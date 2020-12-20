from django.db import models
from django.contrib.auth import settings
from django.contrib.postgres.fields import ArrayField

from utils.misc import empty_array, DiscordIDField


class User(models.Model):
    id = DiscordIDField(primary_key=True)
    name = models.CharField(max_length=32)
    tag = models.CharField(max_length=6)
    avatar = models.URLField(max_length=150, blank=True, default="")
    email = models.CharField(max_length=50, default="", blank=True)  # TODO email validator
    verified = models.BooleanField(default=False)
    perks = models.PositiveIntegerField(default=0)

    def get_avatar_url(self):
        if self.avatar != "":
            return f"https://cdn.discordapp.com/avatars/{self.id}/{self.avatar}.png"
        else:
            return "https://cdn.discordapp.com/embed/avatars/1.png"


class Guild(models.Model):
    id = DiscordIDField(primary_key=True)
    name = models.CharField(max_length=100)
    suggestion_message_id = DiscordIDField()


class GuildOption(models.Model):
    guild: Guild = models.OneToOneField(Guild, on_delete=models.CASCADE, related_name="options")
    event_submission = models.BooleanField(default=False)
    bug_report = models.BooleanField(default=False)
    mod_mail = models.BooleanField(default=False)
    suggestions = models.BooleanField(default=False)


class GuildChannel(models.Model):
    guild: Guild = models.OneToOneField(Guild, on_delete=models.CASCADE, related_name="channels")
    welcome_channel_id = DiscordIDField()
    announcements_channel_id = DiscordIDField()
    react_for_roles_channel_id = DiscordIDField()
    mod_mail_report_channel_id = DiscordIDField()
    bug_reports_channel_id = DiscordIDField()
    code_submissions_channel_id = DiscordIDField()
    suggestions_channel_id = DiscordIDField()
    system_log_channel_id = DiscordIDField()
    deterrence_log_channel_id = DiscordIDField()
    bot_log_channel_id = DiscordIDField()
    successful_verifications_channel_id = DiscordIDField()
    verification_channel_id = DiscordIDField()
    member_count_channel_id = DiscordIDField()
    general_channel_id = DiscordIDField()
    rules_channel_id = DiscordIDField()
    member_log_channel_id = DiscordIDField()
    update_log_channel_id = DiscordIDField()


class GuildRolesSpecial(models.Model):
    guild: Guild = models.OneToOneField(Guild, on_delete=models.CASCADE, related_name="roles_special")
    muted_role_id = DiscordIDField()
    verified_role_id = DiscordIDField()
    trusted_role_id = DiscordIDField()
    new_member_role = DiscordIDField()


class Role(models.Model):
    id = DiscordIDField(primary_key=True)
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="roles")

    class Meta:
        unique_together = (('id', 'guild'),)


class SelfAssignableCategory(models.Model):
    name = models.CharField(max_length=32)
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="self_assignable_categories")

    class Meta:
        unique_together = (('name', 'guild'),)


class SelfAssignableRole(models.Model):
    role: Role = models.OneToOneField(Role, on_delete=models.CASCADE)
    emoji_id = DiscordIDField()
    order = models.PositiveIntegerField()
    category: SelfAssignableCategory = models.ForeignKey(
        SelfAssignableCategory, on_delete=models.CASCADE, related_name="self_assignable_roles"
    )

    class Meta:
        unique_together = (('order', 'category'), ('role', 'emoji_id'))


class Member(models.Model):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="members")
    roles = models.ManyToManyField(Role, blank=True)
    mod_mail = models.BooleanField(default=False)
    member = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True)
    leave_date = models.DateTimeField(null=True, blank=True, default=None)
    invited_by = models.ForeignKey("Invite", on_delete=models.SET_NULL, related_name="members", null=True, blank=True)

    class Meta:
        unique_together = (('user', 'guild'), ('user', 'guild', 'invited_by'))


class Invite(models.Model):
    code = models.CharField(max_length=8, unique=True)
    creator: Member = models.OneToOneField(Member, on_delete=models.CASCADE)


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


class Infraction(models.Model):
    class InfractionsChoice(models.TextChoices):
        MUTE = "M", "Mute"
        KICK = "K", "Kick"
        BAN = "B", "Ban"

    member: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="infractions")
    type = models.CharField(max_length=30, choices=InfractionsChoice.choices)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()


class Rule(models.Model):
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="rules")
    number = models.IntegerField(blank=True)
    name = models.CharField(max_length=20)
    statement = models.TextField()
    alias = ArrayField(models.CharField(max_length=20), default=empty_array)

    class Meta:
        unique_together = (('number', 'guild'),)


class Suggestion(models.Model):
    class SuggestionStatus(models.TextChoices):
        UNDER_REVIEW = "R", "Under Review"
        APPROVED = "A", "Approved"
        DENIED = "D", "Denied"

    message_id = DiscordIDField(primary_key=True)
    author: Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="suggestions")
    guild: Guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name="suggestions")
    brief = models.CharField(max_length=2000)
    status = models.CharField(max_length=20, choices=SuggestionStatus.choices, default=SuggestionStatus.UNDER_REVIEW)
    reason = models.CharField(max_length=2000, default="No reason specified.", blank=True)
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)


class Admin(models.Model):
    auth_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user: User = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin")
    guilds: Guild = models.ManyToManyField(Guild)

    def get_admin_guild_names(self):
        return {guild.id: guild.name for guild in self.guilds.all()}
