# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-25 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20170923_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_vip_demand',
            field=models.BooleanField(default=False, verbose_name='是否已续等'),
        ),
    ]