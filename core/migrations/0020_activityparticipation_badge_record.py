# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-01 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20170901_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityparticipation',
            name='badge_record',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_participation', to='core.BadgeRecord', verbose_name='奖励徽章记录'),
        ),
    ]
