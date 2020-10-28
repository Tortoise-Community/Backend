from django.db import models
from django.contrib.postgres.fields import JSONField

from utils.misc import empty_dict


class Slider(models.Model):
    head_crumb_1 = models.CharField(max_length=20, blank=True)
    head_crumb_2 = models.CharField(max_length=20, blank=True)
    span = models.CharField(max_length=20, blank=True)
    slide_image_url = models.URLField(blank=True)
    sub_head = models.CharField(max_length=50, blank=True)
    note = models.TextField(blank=True)
    button = models.BooleanField(blank=True, default=True)


class News(models.Model):
    class NewsStatus(models.TextChoices):
        NEWS = "News"
        LIVE = "Live"
        ANNOUNCEMENTS = "Announcements"

    news = models.TextField()
    choice = models.CharField(max_length=15, choices=NewsStatus.choices, default=NewsStatus.LIVE)


class Team(models.Model):
    name = models.CharField(max_length=15)
    profile_img = models.ImageField(upload_to='img/team')
    nickname = models.CharField(max_length=15)
    designation = models.CharField(max_length=12)


class Events(models.Model):
    class EventPageThemes(models.TextChoices):
        LIGHT_THEME = "event-light-theme", "Light Theme"
        DARK_THEME = "event-dark-theme", "Dark Theme"
        ARES_THEME = "event-ares-theme", "Ares Theme"
        NEMESIS_THEME = "event-nemesis-theme", "Nemesis Theme"
        GRASS_HOPPER_THEME = "event-grass-hopper-theme", "Grasshopper Theme"

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
    event_image = models.ImageField(upload_to='img/eventimgs', blank=True)
    cover_image = models.ImageField(upload_to='img/bgimgs')
    page_theme = models.CharField(max_length=35, choices=EventPageThemes.choices, default=EventPageThemes.LIGHT_THEME)
    event_type = models.CharField(max_length=17, choices=EventTypes.choices, default=EventTypes.CTF)
    due_date = models.DateField()
    end_date = models.DateField()
    sponsors = JSONField(null=True, default=empty_dict, blank=True)
    winner = models.CharField(max_length=100, blank=True)
    prize = models.CharField(max_length=100)
    status = models.CharField(max_length=17, choices=EventStatus.choices, default=EventStatus.ENDED)
    style = models.CharField(max_length=50, choices=EventPageCodeStyles.choices, default=EventPageCodeStyles.DEFAULT)
    host = models.CharField(max_length=100)
    task = models.CharField(max_length=50)
    desc = models.TextField(default=None)


class Privacy(models.Model):
    header = models.CharField(max_length=150, blank=True)
    content = models.TextField(default=None, blank=True)
    extra = models.TextField(default=None, blank=True, null=True)


class Changes(models.Model):
    date = models.DateField()
    content = models.TextField(default=None)
