# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-15 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_base', '0005_broadcast_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='target',
            field=models.CharField(blank=True, choices=[('TARGET_LIVE', '直播间消息'), ('TARGET_SYSTEM', '系统消息'), ('TARGET_SYSTEM_FAMILYS', '系統消息（家族成員）'), ('TARGET_SYSTEM_NOT_FAMILYS', '系統消息（非家族成員）')], max_length=20, null=True, verbose_name='目标用户'),
        ),
    ]