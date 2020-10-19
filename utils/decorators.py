from userdata.models import Guild
from .mixins import ResponseMixin as Res


def permission_required(func):
    def wrapper(request, guild_id):
        try:
            guild = Guild.objects.get(id=guild_id)
        except Guild.DoesNotExist:
            return Res.http_responce_404(request)
            pass
        if guild in request.user.admins.guild.all():
            return func(request, guild_id)
        else:
            return Res.json_response_404()

    return wrapper
