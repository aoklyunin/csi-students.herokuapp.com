# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-17 17:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sworks', '0003_auto_20170317_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attemptcomment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 17, 17, 32, 39, 136823)),
        ),
        migrations.AlterField(
            model_name='mark',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 17, 17, 32, 39, 142105)),
        ),
    ]
