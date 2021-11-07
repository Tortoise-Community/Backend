from django.db import models


class Paste(models.Model):
    slug = models.SlugField(primary_key=True)
    body = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     app_label = "ide"
