from rest_framework import serializers
from .models import Project, Event


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "pk", "slug", "name", "github",
            "language", "stars", "forks", "commits",
            "short_desc"
        )


class ProjectAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "pk", "slug", "name", "github",
            "language", "stars", "forks", "commits",
            "short_desc", "long_desc"
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "pk", "slug", "name",
            "short_desc", "status",
            "event_tags", "winner_name", "due_date",
            "end_date", "prize", "host", "winner_name"
        )


class EventAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "pk", "slug", "name",
            "end_date", "prize", "host",
            "short_desc", "status", "long_desc",
            "event_tags", "winner_name", "due_date"
        )
