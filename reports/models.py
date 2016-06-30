from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Reports(models.Model):
    ACTIVITY_CHOICES = (
        ('attended', 'Attended an Event'),
        ('organized', 'Organized an Event'),
        ('coorganized', 'Helped Organize an Event with a fellow Ambassador'),
    )
    user = models.ForeignKey('auth.User')
    report_title = models.CharField(max_length=250)
    report_date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=1000)
    activity = models.CharField(choices=ACTIVITY_CHOICES, max_length=11)
    activity_date =  models.DateField()

