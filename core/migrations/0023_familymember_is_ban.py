# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-01 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_familymission_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='is_ban',
            field=models.BooleanField(default=False, verbose_name='是否禁言'),
        ),
    ]
