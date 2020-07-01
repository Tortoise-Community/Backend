from django.db import models


class Slider(models.Model):
    HeadCrumb1 = models.CharField(max_length=20, blank=True)
    Span = models.CharField(max_length=20, blank=True)
    HeadCrumb2 = models.CharField(max_length=20, blank=True)
    Slideimageurl = models.URLField(blank=True) # noqa
    Subhead = models.CharField(max_length=50, blank=True)
    Note = models.TextField(blank=True)
    button = models.BooleanField(blank=True, default=True)


class News(models.Model):
    CHOICE = [
        ("Live", "Live"), ("Announcements", "Announcements"), ("News", "News")
    ]
    news = models.TextField()
    choice = models.CharField(max_length=15, choices=CHOICE, default='Live')


class Team(models.Model):
    name = models.CharField(max_length=15)
    profilepic = models.ImageField(upload_to='img/team') # noqa
    nickname = models.CharField(max_length=15)
    designation = models.CharField(max_length=12)


class Events(models.Model):
    CHOICE = [
        ("Coding-Challenge", "Coding-Challenge"), ("CTF-Event", "CTF-Event")
    ]
    STATUS = [
        ("Upcoming", "Upcoming"), ("Live", "Live"), ("Ended", "Ended")
    ]
    name = models.CharField(max_length=15)
    eventimage = models.ImageField(upload_to='img/eventimgs', blank=True) # noqa
    coverimage = models.ImageField(upload_to='img/bgimgs') # noqa
    eventtype = models.CharField(max_length=17, choices=CHOICE, default='CTF-Event') # noqa
    duedate = models.DateField() # noqa
    enddate = models.DateField() # noqa
    winner = models.CharField(max_length=100, blank=True)
    prize = models.CharField(max_length=100)
    status = models.CharField(max_length=17, choices=STATUS, default='Ended')
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
