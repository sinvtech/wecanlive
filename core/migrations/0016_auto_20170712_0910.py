# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20170712_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='messages',
            field=models.ManyToManyField(blank=True, related_name='families', to='django_base.Message', verbose_name='家族消息'),
        ),
    ]