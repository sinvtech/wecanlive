# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-25 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rankrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rankrecord',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='rankrecord',
            name='rank_type',
        ),
        migrations.AddField(
            model_name='rankrecord',
            name='receive_diamond_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='收到钻石數量'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rankrecord',
            name='send_diamond_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='送出钻石數量'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rankrecord',
            name='star_index_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='元气指数'),
            preserve_default=False,
        ),
    ]