# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-28 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_member_vip_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='vip_level',
            field=models.IntegerField(default=0, verbose_name='VIP等级'),
        ),
    ]