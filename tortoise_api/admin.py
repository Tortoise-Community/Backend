from django.contrib import admin

from tortoise_api import models


admin.site.register(models.User)
admin.site.register(models.Guild)
admin.site.register(models.Role)
admin.site.register(models.Member)
admin.site.register(models.Strike)
admin.site.register(models.MemberWarning)
admin.site.register(models.Infractions)
admin.site.register(models.Rules)
admin.site.register(models.Suggestions)
admin.site.register(models.Admins)
