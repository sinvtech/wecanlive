# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_merge_20170710_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='tencent_sig',
            field=models.TextField(blank=True, default='', help_text='腾讯云SDK产生', verbose_name='腾讯云鉴权密钥'),
        ),
        migrations.AddField(
            model_name='member',
            name='tencent_sig_expire',
            field=models.DateTimeField(blank=True, help_text='默认过期时间为180天', null=True, verbose_name='腾讯云鉴权密钥过期时间'),
        ),
    ]