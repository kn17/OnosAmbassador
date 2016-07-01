# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.TextField(default='name'),
        ),
    ]