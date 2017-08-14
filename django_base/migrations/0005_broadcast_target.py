# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-05 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_base', '0004_auto_20170803_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='broadcast',
            name='target',
            field=models.CharField(blank=True, choices=[('TARGET_LIVE', '直播间消息'), ('TARGET_SYSTEM', '系统消息')], max_length=20, null=True, verbose_name='目标用户'),
        ),
    ]