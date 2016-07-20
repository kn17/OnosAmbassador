from __future__ import unicode_literals
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    image = models.FileField()
    country = CountryField()
    city = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    location = models.TextField()
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Mentor(models.Model):
    mentor = models.ForeignKey(
        UserProfile, models.PROTECT, related_name='mentees',
        limit_choices_to={'user__is_staff': True},
    )
    mentee = models.ForeignKey(
        UserProfile, models.PROTECT, related_name='mentors',
        limit_choices_to={'user__is_staff': False},
    )