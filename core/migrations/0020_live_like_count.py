# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20170711_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='live',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='点赞数量'),
        ),
    ]