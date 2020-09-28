from django.contrib import admin
from .models import Member, Projects, Rules, Suggestions, User, Guild, Role

# Register your models here.
admin.site.register(Member)
admin.site.register(Projects)
admin.site.register(Rules)
admin.site.register(Suggestions)
admin.site.register(User)
admin.site.register(Guild)
admin.site.register(Role)
