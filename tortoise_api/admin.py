from django.contrib import admin

from tortoise_api import models


admin.site.register(models.User)
admin.site.register(models.Guild)
admin.site.register(models.GuildOption)
admin.site.register(models.Role)
admin.site.register(models.Member)
admin.site.register(models.Strike)
admin.site.register(models.MemberWarning)
admin.site.register(models.Infraction)
admin.site.register(models.Rule)
admin.site.register(models.Suggestion)
admin.site.register(models.Admin)
admin.site.register(models.Invite)