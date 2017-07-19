# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170718_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='item_key',
        ),
        migrations.AddField(
            model_name='badge',
            name='badge_item',
            field=models.CharField(choices=[('SEND_PRIZE', '送礼物额度'), ('WATCH_LIVE_DURATION', '观看时长'), ('COUNT_WATCH_LOG', '累计观看数'), ('COUNT_FOLLOWED', '追踪数'), ('COUNT_FRIEND', '好友数'), ('COUNT_LOGIN', '连续登录天数'), ('COUNT_INVITE', '邀请好友注册数'), ('COUNT_ENTER_LIVE', '直播间访谈数'), ('COUNT_SHARE_LIVE', '分享直播间数'), ('COUNT_LIVE', '连续开播的天数'), ('COUNT_RECEIVE_DIAMOND', '收到钻石额度'), ('COUNT_RECEIVE_PRIZE', '收到礼物数量'), ('BINDING_MOBILE', '绑定手机'), ('INFO_COMPLETE', '完善个人资料'), ('LIVE_DURATION', '开播时数'), ('CONTRIBUTION', '贡献值（家族任务限定）'), ('SPECIAL', '特殊')], default='SEND_PRIZE', max_length=50, verbose_name='任务元件'),
        ),
        migrations.AlterField(
            model_name='familymission',
            name='badge',
            field=models.ForeignKey(blank=True, help_text='当选择的奖励元件为徽章时添加', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_missions', to='core.Badge', verbose_name='奖励徽章'),
        ),
    ]
