# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-01 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170831_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_settle',
            field=models.BooleanField(default=False, verbose_name='是否已结算'),
        ),
        migrations.AlterField(
            model_name='activityparticipation',
            name='status',
            field=models.CharField(choices=[('ACTIVE', '进行中'), ('EXPIRED', '超时未达成'), ('COMPLETE', '完成')], default='ACTIVE', max_length=20, verbose_name='参与状态'),
        ),
    ]
