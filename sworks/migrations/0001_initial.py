# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-17 16:11
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(default=datetime.datetime(2017, 3, 17, 16, 11, 47, 575598))),
                ('link', models.CharField(max_length=200)),
                ('state', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['add_date'],
            },
        ),
        migrations.CreateModel(
            name='AttemptComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isReaded', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=2000)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 3, 17, 16, 11, 47, 570820))),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='CodeLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_value', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(default=datetime.datetime(2017, 3, 17, 16, 11, 47, 544753))),
                ('link', models.CharField(max_length=200)),
                ('checked', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PretendToCheat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=0)),
                ('n', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PretendVal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique', models.FloatField(default=0)),
                ('mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sworks.Mark')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000000)),
                ('n', models.IntegerField(default=0)),
                ('link', models.CharField(default='', max_length=1000)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sworks.CodeLanguage')),
            ],
            options={
                'ordering': ['n'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_klass', models.CharField(max_length=200)),
                ('st_group', models.IntegerField()),
                ('marks', models.ManyToManyField(to='sworks.Mark')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('est1', models.CharField(max_length=200)),
                ('est2', models.CharField(max_length=200)),
                ('est3', models.CharField(max_length=200)),
                ('est4', models.CharField(max_length=200)),
                ('est5', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sworks.TaskType'),
        ),
        migrations.AddField(
            model_name='task',
            name='work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sworks.WorkType'),
        ),
        migrations.AddField(
            model_name='pretendval',
            name='programCode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sworks.ProgramCode'),
        ),
        migrations.AddField(
            model_name='pretendval',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sworks.Student'),
        ),
        migrations.AddField(
            model_name='pretendtocheat',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sworks.Task'),
        ),
        migrations.AddField(
            model_name='pretendtocheat',
            name='vals',
            field=models.ManyToManyField(to='sworks.PretendVal'),
        ),
        migrations.AddField(
            model_name='mark',
            name='sources',
            field=models.ManyToManyField(to='sworks.ProgramCode'),
        ),
        migrations.AddField(
            model_name='mark',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sworks.Task'),
        ),
        migrations.AddField(
            model_name='attemptcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sworks.Student'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='comment',
            field=models.ManyToManyField(to='sworks.AttemptComment'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sworks.Student'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sworks.Task'),
        ),
    ]
