# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-01 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20170901_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityparticipation',
            name='prize_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_participation', to='core.PrizeTransaction', verbose_name='礼物奖励记录'),
        ),
    ]
