# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20160622_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
