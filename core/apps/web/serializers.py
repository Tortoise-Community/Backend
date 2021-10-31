from rest_framework import serializers
from .models import Project, Event


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "slug", "name", "description",
            "stars", "forks", "commits", "github"
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "slug", "name",
            "short_desc", "status",
            "end_date", "prize", "host",
            "event_tags", "winner_name", "due_date"
        )

