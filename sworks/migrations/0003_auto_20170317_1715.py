# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-17 17:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sworks', '0002_auto_20170317_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attempt',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='student',
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='task',
        ),
        migrations.RemoveField(
            model_name='pretendtocheat',
            name='task',
        ),
        migrations.RemoveField(
            model_name='pretendtocheat',
            name='vals',
        ),
        migrations.RemoveField(
            model_name='pretendval',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='pretendval',
            name='programCode',
        ),
        migrations.RemoveField(
            model_name='pretendval',
            name='student',
        ),
        migrations.RemoveField(
            model_name='programcode',
            name='language',
        ),
        migrations.RenameField(
            model_name='mark',
            old_name='checked',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='st_klass',
            new_name='github_rep',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='link',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='sources',
        ),
        migrations.RemoveField(
            model_name='student',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='task',
            name='est1',
        ),
        migrations.RemoveField(
            model_name='task',
            name='est2',
        ),
        migrations.RemoveField(
            model_name='task',
            name='est3',
        ),
        migrations.RemoveField(
            model_name='task',
            name='est4',
        ),
        migrations.RemoveField(
            model_name='task',
            name='est5',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_type',
        ),
        migrations.RemoveField(
            model_name='task',
            name='work_type',
        ),
        migrations.AddField(
            model_name='mark',
            name='comment',
            field=models.ManyToManyField(to='sworks.AttemptComment'),
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sworks.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attemptcomment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 17, 17, 14, 54, 502599)),
        ),
        migrations.AlterField(
            model_name='mark',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 17, 17, 14, 54, 507697)),
        ),
        migrations.AlterField(
            model_name='student',
            name='st_group',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Attempt',
        ),
        migrations.DeleteModel(
            name='CodeLanguage',
        ),
        migrations.DeleteModel(
            name='PretendToCheat',
        ),
        migrations.DeleteModel(
            name='PretendVal',
        ),
        migrations.DeleteModel(
            name='ProgramCode',
        ),
        migrations.DeleteModel(
            name='TaskType',
        ),
        migrations.DeleteModel(
            name='WorkType',
        ),
    ]