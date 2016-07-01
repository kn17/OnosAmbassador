from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    image = models.FileField()
    location = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.user.username