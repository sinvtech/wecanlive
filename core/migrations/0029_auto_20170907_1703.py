# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20170907_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='small_level',
            field=models.IntegerField(default=1, verbose_name='小等级'),
        ),
    ]
