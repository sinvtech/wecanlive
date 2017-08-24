# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-23 11:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0039_merge_20170823_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_login', models.DateTimeField(auto_now_add=True, verbose_name='登录时间')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loginrecords_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='activeevent',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
    ]
