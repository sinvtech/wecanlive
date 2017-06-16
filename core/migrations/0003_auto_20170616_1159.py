# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 11:59
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_base', '0002_adminlog'),
        ('core', '0002_member_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('TEXT', '文本'), ('IMAGE', '图片'), ('VIDEO', '视频'), ('AUDIO', '音频'), ('COMBO', '混合'), ('OBJECT', '对象'), ('PROMPT', '提示')], default='TEXT', max_length=20, verbose_name='消息类型')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('params', models.TextField(blank=True, default='', help_text='用 json 存放一些动态的参数', verbose_name='参数')),
                ('audios', models.ManyToManyField(blank=True, related_name='activeevents', to='django_base.AudioModel', verbose_name='音频')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activeevents_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('comments', models.ManyToManyField(blank=True, related_name='activeevents', to='django_base.Comment', verbose_name='评论')),
                ('images', models.ManyToManyField(blank=True, related_name='activeevents', to='django_base.ImageModel', verbose_name='图片')),
                ('videos', models.ManyToManyField(blank=True, related_name='activeevents', to='django_base.VideoModel', verbose_name='视频')),
            ],
            options={
                'verbose_name_plural': '个人动态',
                'db_table': 'core_active_event',
                'verbose_name': '个人动态',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('date_begin', models.DateTimeField(verbose_name='开始时间')),
                ('date_end', models.DateTimeField(verbose_name='结束时间')),
            ],
            options={
                'verbose_name_plural': '活动',
                'db_table': 'core_activity',
                'verbose_name': '活动',
            },
        ),
        migrations.CreateModel(
            name='ActivityParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ACTIVE', '进行中'), ('EXPIRED', '超时未达成'), ('ACTIVE', '完成')], default='ACTIVE', max_length=20, verbose_name='参与状态')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='core.Activity', verbose_name='活动')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activityparticipations_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '活动参与记录',
                'db_table': 'core_activity_participation',
                'verbose_name': '活动参与记录',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('TEXT', '文本'), ('IMAGE', '图片'), ('VIDEO', '视频'), ('AUDIO', '音频'), ('COMBO', '混合'), ('OBJECT', '对象'), ('PROMPT', '提示')], default='TEXT', max_length=20, verbose_name='消息类型')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('params', models.TextField(blank=True, default='', help_text='用 json 存放一些动态的参数', verbose_name='参数')),
                ('excerpt', models.CharField(blank=True, default='', max_length=150, verbose_name='摘要')),
                ('is_done', models.BooleanField(default=False, verbose_name='是否处理')),
                ('audios', models.ManyToManyField(blank=True, related_name='feedbacks', to='django_base.AudioModel', verbose_name='音频')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('images', models.ManyToManyField(blank=True, related_name='feedbacks', to='django_base.ImageModel', verbose_name='图片')),
                ('videos', models.ManyToManyField(blank=True, related_name='feedbacks', to='django_base.VideoModel', verbose_name='视频')),
            ],
            options={
                'verbose_name_plural': '反馈',
                'db_table': 'core_feedback',
                'verbose_name': '反馈',
            },
        ),
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.CharField(choices=[('PENDING', '等待处理'), ('SUCCESS', '举报成功'), ('FAIL', '举报失败')], default='PENDING', max_length=20, verbose_name='状态')),
                ('excerpt', models.CharField(blank=True, default='', max_length=150, verbose_name='摘要')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='informs_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('images', models.ManyToManyField(blank=True, related_name='informs', to='django_base.ImageModel', verbose_name='图片')),
            ],
            options={
                'verbose_name_plural': '举报',
                'db_table': 'core_inform',
                'verbose_name': '举报',
            },
        ),
        migrations.CreateModel(
            name='LevelOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': ('等级设定',),
                'db_table': 'core_level_option',
                'verbose_name': ('等级设定',),
            },
        ),
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('password', models.CharField(max_length=45, verbose_name='房间密码')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lives_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('comments', models.ManyToManyField(blank=True, related_name='lives', to='django_base.Comment', verbose_name='评论')),
            ],
            options={
                'verbose_name_plural': '直播',
                'db_table': 'core_live',
                'verbose_name': '直播',
            },
        ),
        migrations.CreateModel(
            name='LiveBarrage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('TEXT', '文本'), ('IMAGE', '图片'), ('VIDEO', '视频'), ('AUDIO', '音频'), ('COMBO', '混合'), ('OBJECT', '对象'), ('PROMPT', '提示')], default='TEXT', max_length=20, verbose_name='消息类型')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('params', models.TextField(blank=True, default='', help_text='用 json 存放一些动态的参数', verbose_name='参数')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('audios', models.ManyToManyField(blank=True, related_name='livebarrages', to='django_base.AudioModel', verbose_name='音频')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livebarrages_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('images', models.ManyToManyField(blank=True, related_name='livebarrages', to='django_base.ImageModel', verbose_name='图片')),
                ('live', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barrages', to='core.Live', verbose_name='直播')),
                ('videos', models.ManyToManyField(blank=True, related_name='livebarrages', to='django_base.VideoModel', verbose_name='视频')),
            ],
            options={
                'verbose_name_plural': '直播弹幕',
                'db_table': 'core_live_barrage',
                'verbose_name': '直播弹幕',
            },
        ),
        migrations.CreateModel(
            name='LiveWatchLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enter', models.DateTimeField(verbose_name='进入时间')),
                ('date_leave', models.DateTimeField(verbose_name='退出时间')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livewatchlogs_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('live', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_logs', to='core.Live', verbose_name='直播')),
            ],
            options={
                'verbose_name_plural': '直播观看记录',
                'db_table': 'core_live_watch_log',
                'verbose_name': '直播观看记录',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('embed_link', models.URLField(verbose_name='嵌入链接')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '影片节目',
                'db_table': 'core_movie',
                'verbose_name': '影片节目',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificationss_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '通知',
                'db_table': 'core_notification',
                'verbose_name': '通知',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '礼物',
                'db_table': 'core_prize',
                'verbose_name': '礼物',
            },
        ),
        migrations.CreateModel(
            name='PrizeTransition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='金额')),
                ('remark', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transitions', to='core.Prize', verbose_name='礼物')),
                ('user_credit', models.ForeignKey(blank=True, help_text='即余额减少的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prizetransitions_credit', to=settings.AUTH_USER_MODEL, verbose_name='贷方用户')),
                ('user_debit', models.ForeignKey(blank=True, help_text='即余额增加的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prizetransitions_debit', to=settings.AUTH_USER_MODEL, verbose_name='借方用户')),
            ],
            options={
                'verbose_name_plural': '礼物记录',
                'db_table': 'core_prize_transition',
                'verbose_name': '礼物记录',
            },
        ),
        migrations.CreateModel(
            name='RedBagRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redbagrecords_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('live', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='red_bag_records', to='core.Live', verbose_name='直播')),
            ],
            options={
                'verbose_name_plural': '红包记录',
                'db_table': 'core_red_bag_record',
                'verbose_name': '红包记录',
            },
        ),
        migrations.CreateModel(
            name='StarBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '星光宝盒',
                'db_table': 'core_star_box',
                'verbose_name': '星光宝盒',
            },
        ),
        migrations.CreateModel(
            name='StarBoxRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='获得时间')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='starboxrecords_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('live', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='star_box_records', to='core.Live', verbose_name='直播')),
                ('star_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='core.StarBox', verbose_name='星光宝盒')),
            ],
            options={
                'verbose_name_plural': '星光宝盒记录',
                'db_table': 'core_star_box_record',
                'verbose_name': '星光宝盒记录',
            },
        ),
        migrations.CreateModel(
            name='StarMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '星光任务',
                'db_table': 'core_star_mission',
                'verbose_name': '星光任务',
            },
        ),
        migrations.CreateModel(
            name='StarMissionAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='starmissionachievements_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='core.StarMission', verbose_name='任务')),
            ],
            options={
                'verbose_name_plural': '星光任务成果',
                'db_table': 'core_star_mission_achievement',
                'verbose_name': '星光任务成果',
            },
        ),
        migrations.CreateModel(
            name='StatisticRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('date_begin', models.DateTimeField(verbose_name='开始时间')),
                ('date_end', models.DateTimeField(verbose_name='结束时间')),
            ],
            options={
                'verbose_name_plural': '统计规则',
                'db_table': 'core_rule',
                'verbose_name': '统计规则',
            },
        ),
        migrations.CreateModel(
            name='VisitLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_lng', models.FloatField(blank=True, default=0, verbose_name='经度')),
                ('geo_lat', models.FloatField(blank=True, default=0, verbose_name='纬度')),
                ('radius', models.FloatField(blank=True, default=0, verbose_name='半径')),
                ('geo_label', models.CharField(blank=True, default='', max_length=255, verbose_name='位置标签')),
                ('adcode', models.IntegerField(default=0, help_text='保存时试图自动获取区划编码', verbose_name='行政区划编码')),
                ('geo_info', models.TextField(blank=True, default='', help_text='保存时自动尝试获取地理信息', verbose_name='地理信息')),
                ('date_last_visit', models.DateTimeField(auto_now=True, verbose_name='最后访问时间')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visitlogs_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_logs', to=settings.AUTH_USER_MODEL, verbose_name='被访问用户')),
            ],
            options={
                'verbose_name_plural': '访客记录',
                'db_table': 'core_visit_log',
                'verbose_name': '访客记录',
            },
        ),
        migrations.AddField(
            model_name='family',
            name='award_element_settings',
            field=models.TextField(blank=True, default='', help_text='JSON字段，后台设定设定各类奖励元件的开关以及数量，逻辑需要额外定义，前端做对应的实现', verbose_name='奖励元件设置'),
        ),
        migrations.AddField(
            model_name='family',
            name='date_mission_unlock',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0), verbose_name='发布任务解锁日期'),
        ),
        migrations.AddField(
            model_name='family',
            name='level_settings',
            field=models.TextField(blank=True, default='', help_text='JSON字段，后台设定设定家族等级规则，包括等级分段、所需贡献值以及颜色逻辑需要额外定义，前端做对应的实现', verbose_name='家族等级设定'),
        ),
        migrations.AddField(
            model_name='family',
            name='logo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family', to='django_base.ImageModel', verbose_name='图标'),
        ),
        migrations.AddField(
            model_name='family',
            name='mission_element_settings',
            field=models.TextField(blank=True, default='', help_text='JSON字段，后台设定设定各类任务元件的开关以及数量，逻辑需要额外定义，前端做对应的实现', verbose_name='任务元件设置'),
        ),
        migrations.AddField(
            model_name='family',
            name='mission_unlock_duration',
            field=models.IntegerField(default=0, help_text='后台设置的家族发布任务时间间隔（秒），发布了任务之后距离下个任务之间需要间隔这个时间', verbose_name='发布任务时间间隔'),
        ),
        migrations.AlterUniqueTogether(
            name='activityparticipation',
            unique_together=set([('activity', 'author')]),
        ),
    ]