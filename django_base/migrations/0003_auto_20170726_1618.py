# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-26 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_base', '0002_menu_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminlog',
            name='level',
        ),
        migrations.AddField(
            model_name='adminlog',
            name='type',
            field=models.CharField(choices=[('CREATE', '新建'), ('UPDATE', '修改'), ('DELETE', '刪除')], default=None, max_length=20, verbose_name='修改类型'),
            preserve_default=False,
        ),
    ]
