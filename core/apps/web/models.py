from django.db import models


class Event(models.Model):
    class EventTypes(models.TextChoices):
        OTHER = "Other Event", "Other"
        CTF = "CTF Event", "CTF-Event"
        TEAM_CHALLENGE = "Team Challenge", "Team-Challenge"
        CODING_CHALLENGE = "Coding Challenge", "Coding-Challenge"

    class EventStatus(models.TextChoices):
        LIVE = "Live"
        ENDED = "Ended"
        UPCOMING = "Upcoming"

    class EventPageCodeStyles(models.TextChoices):
        DEFAULT = "default.min.css", "Default"
        DARK = "dark.min.css", "Dark"
        DRACULA = "dracula.min.css", "Dracula"
        TOMORROW = "tomorrow.min.css", "Tomorrow"
        NIGHT_OWL = "night-owl.min.css", "Night Owl"
        CODEPEN = "codepen-embed.min.css", "Codepen"
        GITHUB_GIST = "github-gist.min.css", "Github Gist"
        ATOM_DARK = "atom-one-dark.min.css", "Atom Dark"
        SOLARIZED_DARK = "solarized-dark.min.css", "Solarized Dark"
        ATELIER_CAVE = "atelier-cave-dark.min.css", "Atelier Cave"
        TOMORROW_NIGHT_BLUE = "tomorrow-night-blue.css", "Tomorrow Night Blue"
        ATOM_DARK_REASONABLE = "atom-one-dark-reasonable.min.css", "Atom Dark Reasonable"

    name = models.CharField(max_length=15)
    prize = models.CharField(max_length=150)
    host = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=17, choices=EventStatus.choices, default=EventStatus.ENDED)
    event_type = models.CharField(max_length=17, choices=EventTypes.choices, default=EventTypes.CTF)
    style = models.CharField(max_length=50, choices=EventPageCodeStyles.choices, default=EventPageCodeStyles.DEFAULT)
    due_date = models.DateField()
    end_date = models.DateField()


class Project(models.Model):
    name = models.CharField(max_length=15)
    brief = models.TextField()
    github = models.URLField(blank=True)
    commits = models.PositiveSmallIntegerField(blank=True, default=0)
    stars = models.PositiveSmallIntegerField(blank=True, default=0)
    forks = models.PositiveSmallIntegerField(blank=True, default=0)
    contributors = models.PositiveSmallIntegerField(blank=True, default=0)
