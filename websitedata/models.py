from django.db import models
from django.contrib.postgres.fields import JSONField

from utils.misc import code_hljs_styles, news_update_types, event_status, event_types, page_theme_choices, empty_dict


class Slider(models.Model):
    head_crumb_1 = models.CharField(max_length=20, blank=True)
    head_crumb_2 = models.CharField(max_length=20, blank=True)
    span = models.CharField(max_length=20, blank=True)
    slide_image_url = models.URLField(blank=True)
    sub_head = models.CharField(max_length=50, blank=True)
    note = models.TextField(blank=True)
    button = models.BooleanField(blank=True, default=True)


class News(models.Model):
    news = models.TextField()
    choice = models.CharField(max_length=15, choices=news_update_types, default='Live')


class Team(models.Model):
    name = models.CharField(max_length=15)
    profile_img = models.ImageField(upload_to='img/team')
    nickname = models.CharField(max_length=15)
    designation = models.CharField(max_length=12)


class Events(models.Model):
    name = models.CharField(max_length=15)
    event_image = models.ImageField(upload_to='img/eventimgs', blank=True)
    cover_image = models.ImageField(upload_to='img/bgimgs')
    page_theme = models.CharField(max_length=35, choices=page_theme_choices, default='event-light-theme')
    event_type = models.CharField(max_length=17, choices=event_types, default='CTF-Event')
    due_date = models.DateField()
    end_date = models.DateField()
    sponsors = JSONField(null=True, default=empty_dict, blank=True)
    winner = models.CharField(max_length=100, blank=True)
    prize = models.CharField(max_length=100)
    status = models.CharField(max_length=17, choices=event_status, default='Ended')
    style = models.CharField(max_length=50, choices=code_hljs_styles, default='default.min.css')
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
