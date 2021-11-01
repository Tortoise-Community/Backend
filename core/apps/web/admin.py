from django.contrib import admin

from .models import Project, Event

admin.site.register(Event)
admin.site.register(Project)
