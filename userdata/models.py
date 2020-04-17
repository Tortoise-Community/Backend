from django.db import models
from Tortoise import settings
from django.contrib.postgres.fields import ArrayField,JSONField

def default_array():
    return []

def default_strikes():
    return {"AD":0,
            "Racial":0,
            "Homo":0,
            "Common":0
            } 
def default_status():
	return {}            
            
def default_json():
	return {"status":"Offline","last_down_time":"","time_went_down":""}
# Create your models here.


class Members(models.Model):
    name = models.CharField(max_length=100,default=None,blank=True,null=True)
    tag = models.CharField(max_length=6,blank=True,null=True)
    user_id = models.BigIntegerField(primary_key=True)
    guild_id = models.BigIntegerField()
    email = models.TextField(blank=True, null=True)
    perks = models.IntegerField(blank=True, null=True)
    join_date = models.DateTimeField(blank=True,null = True)
    leave_date = models.DateTimeField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null= True,default=False)
    strikes = JSONField(null=True,default=default_strikes)
    mod_mail = models.BooleanField(blank=True, null=True,default=False)
    warnings = ArrayField(models.CharField(max_length=300),null=True,default=default_array,blank=True)
    roles = ArrayField(models.BigIntegerField(),null=True,default=default_array,blank=True)
    muted_until = models.DateTimeField(blank=True, null=True)
    member = models.BooleanField(blank=True,null=True,default=False)

    class Meta:
        unique_together = (('user_id', 'guild_id'),)


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
    commits = models.IntegerField(blank=True,null=True)
    stars = models.IntegerField(blank=True,null=True)
    forks = models.IntegerField(blank=True,null=True)
    contributors = models.IntegerField(blank=True,null=True)

class Rules(models.Model):
    number = models.IntegerField(blank=True,null=True)
    statement = models.TextField(blank=True,null=True)
    alias = ArrayField(models.CharField(max_length=20),null=True,default=default_array,blank=True) 
    
class ServerUtils(models.Model):
	guild_id = models.BigIntegerField(primary_key=True)
	event_status = models.BooleanField(default=False)
	bug_report = models.BooleanField(default=False)
	mod_mail = models.BooleanField(default=False)
	bot_status = JSONField(null=True,default=default_status,blank=True) 
	Github_Microservice = JSONField(null=True,default=default_json)
	Status_Microservice = JSONField(null=True,default=default_json)
	Tortoise_BOT = JSONField(null=True,default=default_json)
	Tortoise_BOT2 = JSONField(null=True,default=default_json)
	Website = JSONField(null=True,default=default_json)
	Sockets = JSONField(null=True,default=default_json)
'''  
class TopMember(models.Model):
    name = models.CharField(max_length=100,default=None,blank=True,null=True)
    tag = models.CharField(max_length=6,blank=True,null=True)
    perks = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100,default=None,blank=True,null=True)
    level = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=15,default=None,blank=True,null=True)
    no =  models.IntegerField(blank=True,null=True)'''
    


