# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20160707_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
