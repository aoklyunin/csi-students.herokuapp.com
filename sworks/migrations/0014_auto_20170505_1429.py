# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-05 11:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sworks', '0013_auto_20170424_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100000)),
                ('subText', models.TextField(max_length=100000)),
                ('appendText', models.TextField(max_length=100000)),
            ],
        ),
        migrations.AlterField(
            model_name='attemptcomment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 11, 29, 41, 646746, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mark',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 14, 29, 41, 647746)),
        ),
    ]