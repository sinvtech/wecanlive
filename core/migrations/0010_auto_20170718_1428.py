# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170718_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familymission',
            old_name='item',
            new_name='mission_item',
        ),
        migrations.RemoveField(
            model_name='familymission',
            name='item_value',
        ),
        migrations.AddField(
            model_name='familymission',
            name='award_item',
            field=models.CharField(choices=[('EXPERIENCE_POINTS', '经验值'), ('ICOIN', 'i币'), ('COIN', '金币'), ('PRIZE', '礼物'), ('CONTRIBUTION', '贡献值'), ('BADGE', '勋章'), ('MARQUEE_CONTENT', '跑马灯内容'), ('STAR', '元气')], default='EXPERIENCE_POINTS', max_length=50, verbose_name='奖励元件'),
        ),
        migrations.AddField(
            model_name='familymission',
            name='award_item_value',
            field=models.IntegerField(blank=True, default=0, help_text='指定条件达到后的奖励', verbose_name='奖励元件数值'),
        ),
        migrations.AddField(
            model_name='familymission',
            name='badge',
            field=models.ForeignKey(blank=True, help_text='当选择的奖励元件为勋章时添加', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_missions', to='core.Badge', verbose_name='奖励勋章'),
        ),
        migrations.AddField(
            model_name='familymission',
            name='mission_item_value',
            field=models.IntegerField(blank=True, default=0, help_text='指定条件达到所需的数值', verbose_name='任务元件数值'),
        ),
        migrations.AddField(
            model_name='familymission',
            name='prize',
            field=models.ForeignKey(blank=True, help_text='当选择的奖励元件为礼物时添加', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_missions', to='core.Prize', verbose_name='奖励礼物'),
        ),
    ]
