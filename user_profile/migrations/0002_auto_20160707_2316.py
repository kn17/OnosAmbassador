# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 23:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='location',
            new_name='country',
        ),
    ]
