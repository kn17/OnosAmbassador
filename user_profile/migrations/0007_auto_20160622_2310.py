# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20160622_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(upload_to=b''),
        ),
    ]