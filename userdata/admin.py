from django.contrib import admin
from .models import Members, Projects, Rules, ServerUtils, Developers, Suggestions

# Register your models here.
admin.site.register(Members)
admin.site.register(Projects)
admin.site.register(Rules)
admin.site.register(ServerUtils)
admin.site.register(Developers)
admin.site.register(Suggestions)
