from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify


class Event(models.Model):
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

    slug = models.SlugField(auto_created=True, blank=True, unique=True)
    name = models.CharField(max_length=15)
    prize = models.CharField(max_length=150)
    host = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=300)
    long_desc = models.TextField()
    event_type = ArrayField(models.CharField(max_length=20), size=5, help_text="You can add 5 labels (max)")
    style = models.CharField(max_length=50, choices=EventPageCodeStyles.choices, default=EventPageCodeStyles.DEFAULT)
    due_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    @property
    def status(self):
        return "Ended"

    @property
    def host_name(self):
        return self.host


class Project(models.Model):
    slug = models.SlugField(auto_created=True, blank=True, unique=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    brief = models.TextField()
    github = models.URLField(blank=True)
    commits = models.PositiveSmallIntegerField(blank=True, default=0)
    stars = models.PositiveSmallIntegerField(blank=True, default=0)
    forks = models.PositiveSmallIntegerField(blank=True, default=0)
    contributors = models.PositiveSmallIntegerField(blank=True, default=0)

    def save(self, *args, **kwargs):
        self.slug = self.github.rsplit("/")[-1].lower()
        super(Project, self).save(*args, **kwargs)

    @property
    def language(self):
        return "Python"
