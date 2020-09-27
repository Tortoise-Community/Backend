from django.contrib import admin
from .models import Member, Projects, Rules, Suggestions

# Register your models here.
admin.site.register(Member)
admin.site.register(Projects)
admin.site.register(Rules)
admin.site.register(Suggestions)
