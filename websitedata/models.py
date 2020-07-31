from django.db import models
from utils.misc import code_hljs_styles, news_update_types, event_status, event_types


class Slider(models.Model):
    HeadCrumb1 = models.CharField(max_length=20, blank=True)
    Span = models.CharField(max_length=20, blank=True)
    HeadCrumb2 = models.CharField(max_length=20, blank=True)
    Slideimageurl = models.URLField(blank=True)
    Subhead = models.CharField(max_length=50, blank=True)
    Note = models.TextField(blank=True)
    button = models.BooleanField(blank=True, default=True)


class News(models.Model):
    news = models.TextField()
    choice = models.CharField(max_length=15, choices=news_update_types, default='Live')


class Team(models.Model):
    name = models.CharField(max_length=15)
    profilepic = models.ImageField(upload_to='img/team')
    nickname = models.CharField(max_length=15)
    designation = models.CharField(max_length=12)


class Events(models.Model):
    name = models.CharField(max_length=15)
    eventimage = models.ImageField(upload_to='img/eventimgs', blank=True)
    coverimage = models.ImageField(upload_to='img/bgimgs')
    eventtype = models.CharField(max_length=17, choices=event_types, default='CTF-Event')
    duedate = models.DateField()
    enddate = models.DateField()
    winner = models.CharField(max_length=100, blank=True)
    prize = models.CharField(max_length=100)
    status = models.CharField(max_length=17, choices=event_status, default='Ended')
    style = models.CharField(max_length=25, choices=code_hljs_styles, default='default.min.css')
    host = models.CharField(max_length=15)
    task = models.CharField(max_length=50)
    desc = models.TextField(default=None)


class Privacy(models.Model):
    header = models.CharField(max_length=150, blank=True)
    content = models.TextField(default=None, blank=True)
    extra = models.TextField(default=None, blank=True, null=True)


class Changes(models.Model):
    date = models.DateField()
    content = models.TextField(default=None)
