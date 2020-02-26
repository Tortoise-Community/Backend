from django.db import models
from Tortoise import settings

# Create your models here.

class Slider(models.Model):
    HeadCrumb1 = models.CharField(max_length=20)
    Span = models.CharField(max_length=20,blank=True)
    HeadCrumb2 = models.CharField(max_length=20,blank=True)
    Slideimage = models.ImageField(upload_to='img')
    Subhead = models.CharField(max_length=50,blank=True)
    Note = models.TextField(blank=True)
    
class News(models.Model):
    CHOICE = [
        ("Live","Live"),("Announcements","Announcements"),("News","News")
    ]
    news = models.TextField()
    choice = models.CharField(max_length=15,choices=CHOICE,default='Live')
    
class Team(models.Model):
    name = models.CharField(max_length=15)
    profilepic = models.ImageField(upload_to='img/team')
    nickname = models.CharField(max_length=15)
    designation = models.CharField(max_length=12)

class Events(models.Model):
    CHOICE = [
        ("Coding-Challenge","Coding-Challenge"),("CTF-Event","CTF-Event")
    ]
    STATUS = [
        ("Upcoming","Upcoming"),("Live","Live"),("Ended","Ended")
    ]
    name = models.CharField(max_length=15)
    eventimage = models.ImageField(upload_to='img/eventimgs',blank=True)
    coverimage = models.ImageField(upload_to='img/bgimgs')
    eventtype = models.CharField(max_length=17,choices=CHOICE,default='CTF-Event')
    duedate = models.DateField()
    enddate = models.DateField()
    winner = models.CharField(max_length=100,blank=True)
    prize = models.CharField(max_length=100)
    status = models.CharField(max_length=17,choices=STATUS,default='Ended')
    host = models.CharField(max_length=15)
    task = models.CharField(max_length=50)
    desc = models.TextField(default=None)




class Projects(models.Model):
    STATUS = [
        ("cata yellow","Completed"),("cata purple","Refactoring"),('cata red','Started'),('cata green','Upcoming')
    ]
    name = models.CharField(max_length=15)
    coverimage = models.ImageField(upload_to='img/bgimgs')
    rating = models.FloatField(default=None,blank=True)
    label =  models.CharField(max_length=100,default=None)
    brief = models.TextField(default=None)
    status = models.CharField(max_length=16,choices = STATUS ,default = 'Upcoming')
    github =  models.URLField(blank=True)
    invite = models.URLField(blank=True)
    


class Privacy(models.Model):
    header = models.CharField(max_length=150,blank=True)
    content = models.TextField(default=None,blank=True)
    extra  = models.TextField(default=None,blank=True,null=True)


class Changes(models.Model):
    date = models.DateField()
    content = models.TextField(default=None)