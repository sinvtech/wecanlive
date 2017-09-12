# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-12 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_base', '0009_merge_20170815_1712'),
        ('core', '0035_auto_20170911_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='live',
            name='end_scene_img',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='live', to='django_base.ImageModel', verbose_name='直播结束截图'),
        ),
    ]
