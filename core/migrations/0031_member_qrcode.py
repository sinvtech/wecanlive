# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-09 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_base', '0009_merge_20170815_1712'),
        ('core', '0030_experiencetransaction_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='qrcode',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='django_base.ImageModel', verbose_name='二维码'),
        ),
    ]