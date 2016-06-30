from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event (models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=255)
    date = models.DateField()
    date_created = models.DateField(default=datetime.date.today())
    time = models.TimeField()
    organized_by = models.CharField(max_length= 255)
    location = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

