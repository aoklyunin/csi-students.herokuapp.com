# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-17 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sworks', '0006_auto_20170417_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attemptcomment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 17, 15, 29, 53, 573617)),
        ),
        migrations.AlterField(
            model_name='attemptcomment',
            name='text',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='mark',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 17, 15, 29, 53, 578503)),
        ),
    ]