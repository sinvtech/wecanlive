# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-30 16:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0053_member_stream_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='check_member_history',
        ),
        migrations.AddField(
            model_name='member',
            name='check_member_history',
            field=models.ManyToManyField(blank=True, related_name='user_check', to=settings.AUTH_USER_MODEL, verbose_name='查看谁看过我列表记录'),
        ),
    ]