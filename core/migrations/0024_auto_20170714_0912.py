# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-14 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20170713_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starmissionachievement',
            name='live',
        ),
        migrations.AddField(
            model_name='prizeorder',
            name='star_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prize_orders', to='core.CreditStarTransaction', verbose_name='观众消耗星光记录'),
        ),
    ]