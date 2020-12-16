from django.contrib.auth.models import User as AuthUser

from tortoise_api.models import Admin, Guild


def get_admin_guild_list(guilds):
    tortoise_guilds = Guild.objects.all().values_list("id", flat=True)
    return [
        guild["id"] for guild in guilds if int(guild["permissions"]) & 8 and int(guild["id"]) in tortoise_guilds
    ]


def update_guilds(instance: Admin, guild_list: list):
    if instance.guild is not None:
        instance.guild.clear()
    instance.guild.add(*guild_list)
    instance.save()


def create_admin(user_json: dict, admin_guilds: list, password: str):
    auth_user = AuthUser.objects.create_user(
        username=user_json["id"],
        password=password,
        is_staff=True,
        first_name=user_json["username"],
        email=user_json["email"]
    )
    admin_user = Admin.objects.create(authuser=auth_user, user_id=user_json["id"])
    update_guilds(admin_user, admin_guilds)
    return auth_user
