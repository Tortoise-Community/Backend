from django.contrib.auth.models import User as AuthUser
from userdata.models import Admins, User as MUser, Guild


def create_or_update_admin(user_json: dict, admin_guilds: list, password: str):
    auth_user = AuthUser.objects.create_user(username=user_json["id"],
                                             password=password,
                                             is_staff=True,
                                             first_name=user_json["username"],
                                             email=user_json["email"]
                                             )
    user = MUser.objects.get(id=user_json["id"])
    Admins.objects.create(authuser=auth_user, user=user)
