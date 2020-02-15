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

# Create your models here.


class Members(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    guild_id = models.BigIntegerField()
    email = models.TextField(blank=True, null=True)
    perks = models.IntegerField(blank=True, null=True)
    join_date = models.DateTimeField(blank=True,null = True)
    leave_date = models.DateTimeField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null= True,default=False)
    strikes = JSONField(null=True,default=default_strikes)
    mod_mail = models.BooleanField(blank=True, null=True,default=False)
    warnings = ArrayField(models.CharField(max_length=300),null=True,default=default_array)
    roles = ArrayField(models.IntegerField(),null=True,default=default_array)
    muted_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = (('user_id', 'guild_id'),)
