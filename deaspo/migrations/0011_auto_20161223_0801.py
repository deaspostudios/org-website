# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-23 05:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deaspo', '0010_auto_20161223_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productweborder',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 23, 8, 1, 30, 529000), editable=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default='D:/Users/polyc/PycharmProjects/deaspo_inc/deaspo/media/profile.png', upload_to='profile_images'),
        ),
    ]
