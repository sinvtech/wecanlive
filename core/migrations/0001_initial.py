# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_base', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
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
                'verbose_name': '奖章',
                'db_table': 'core_badge',
                'verbose_name_plural': '奖章',
            },
        ),
        migrations.CreateModel(
            name='CreditCoinTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='金额')),
                ('remark', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
            ],
            options={
                'verbose_name': ('金币流水',),
                'db_table': 'core_credit_coin_transaction',
                'verbose_name_plural': ('金币流水',),
            },
        ),
        migrations.CreateModel(
            name='CreditDiamondTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='金额')),
                ('remark', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
            ],
            options={
                'verbose_name': ('钻石流水',),
                'db_table': 'core_credit_diamond_transaction',
                'verbose_name_plural': ('钻石流水',),
            },
        ),
        migrations.CreateModel(
            name='CreditStarIndexTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='金额')),
                ('remark', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
            ],
            options={
                'verbose_name': ('星光指数流水',),
                'db_table': 'core_credit_star_index_transaction',
                'verbose_name_plural': ('星光指数流水',),
            },
        ),
        migrations.CreateModel(
            name='CreditStarTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='金额')),
                ('remark', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
            ],
            options={
                'verbose_name': ('星星流水',),
                'db_table': 'core_credit_star_transaction',
                'verbose_name_plural': ('星星流水',),
            },
        ),
        migrations.CreateModel(
            name='DailyCheckInLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='签到时间')),
            ],
            options={
                'verbose_name': ('每日签到',),
                'db_table': 'core_daily_check_in_log',
                'verbose_name_plural': ('每日签到',),
            },
        ),
        migrations.CreateModel(
            name='Family',
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
                'verbose_name': '家族',
                'db_table': 'core_family',
                'verbose_name_plural': '家族',
            },
        ),
        migrations.CreateModel(
            name='FamilyArticle',
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
                'verbose_name': '家族文章',
                'db_table': 'core_family_article',
                'verbose_name_plural': '家族文章',
            },
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='称号')),
                ('join_message', models.CharField(help_text='用户在申请加入家族的时候填写的信息', max_length=255, verbose_name='加入信息')),
                ('status', models.CharField(choices=[('PENDING', '等待审批'), ('REJECTED', '被拒绝'), ('APPROVED', '已通过'), ('BLACKLISTED', '黑名单')], max_length=20, verbose_name='是否审批通过')),
                ('role', models.CharField(choices=[('MASTER', '族长'), ('ADMIN', '管理员'), ('NORMAL', '平民')], default='NORMAL', max_length=20, verbose_name='角色')),
            ],
            options={
                'verbose_name': '家族成员',
                'db_table': 'core_family_member',
                'verbose_name_plural': '家族成员',
            },
        ),
        migrations.CreateModel(
            name='FamilyMission',
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
                'verbose_name': '家族任务',
                'db_table': 'core_family_mission',
                'verbose_name_plural': '家族任务',
            },
        ),
        migrations.CreateModel(
            name='FamilyMissionAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '家族任务成就',
                'db_table': 'core_family_mission_achievement',
                'verbose_name_plural': '家族任务成就',
            },
        ),
        migrations.CreateModel(
            name='LiveCategory',
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
                'verbose_name': '直播分类',
                'db_table': 'core_live_category',
                'verbose_name_plural': '直播分类',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('geo_lng', models.FloatField(blank=True, default=0, verbose_name='经度')),
                ('geo_lat', models.FloatField(blank=True, default=0, verbose_name='纬度')),
                ('radius', models.FloatField(blank=True, default=0, verbose_name='半径')),
                ('geo_label', models.CharField(blank=True, default='', max_length=255, verbose_name='位置标签')),
                ('adcode', models.IntegerField(default=0, help_text='保存时试图自动获取区划编码', verbose_name='行政区划编码')),
                ('geo_info', models.TextField(blank=True, default='', help_text='保存时自动尝试获取地理信息', verbose_name='地理信息')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='member', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('nickname', models.CharField(blank=True, default='', max_length=255, verbose_name='昵称')),
                ('nickname_pinyin', models.CharField(blank=True, default='', max_length=255, verbose_name='昵称拼音')),
                ('gender', models.CharField(blank=True, choices=[('', '保密'), ('M', '男'), ('F', '女')], default='', max_length=1, verbose_name='性别')),
                ('real_name', models.CharField(blank=True, default='', max_length=150, verbose_name='真实姓名')),
                ('mobile', models.CharField(max_length=45, unique=True, verbose_name='手机号码')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('search_history', models.TextField(blank=True, help_text='最近10次搜索历史，逗号分隔', null=True, verbose_name='搜索历史')),
                ('signature', models.TextField(blank=True, null=True, verbose_name='个性签名')),
                ('address', models.TextField(blank=True, default='', verbose_name='详细地址')),
                ('session_key', models.CharField(blank=True, default='', help_text='用于区分单用例登录', max_length=255, verbose_name='session_key')),
                ('constellation', models.CharField(blank=True, choices=[('ARIES', '白羊座'), ('TAURUS', '金牛座'), ('GEMINI', '双子座'), ('CANCER', '巨蟹座'), ('LEO', '狮子座'), ('VIRGO', '处女座'), ('LIBRA', '天秤座'), ('SCORPIO', '天蝎座'), ('SAGITTARIUS', '射手座'), ('CAPRICORN', '摩羯座'), ('AQUARIUS', '水瓶座'), ('PISCES', '双鱼座')], default='', max_length=45, verbose_name='星座')),
                ('avatar', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='django_base.ImageModel', verbose_name='头像')),
                ('tags', models.ManyToManyField(blank=True, related_name='members', to='django_base.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '会员',
                'db_table': 'core_member',
                'verbose_name_plural': '会员',
            },
        ),
        migrations.AddField(
            model_name='familymissionachievement',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='familymissionachievements_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='familymissionachievement',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='core.FamilyMission', verbose_name='任务'),
        ),
        migrations.AddField(
            model_name='familymission',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='familymissions_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='familymission',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missions', to='core.Family', verbose_name='家族'),
        ),
        migrations.AddField(
            model_name='familymember',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='familymembers_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='familymember',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='core.Family', verbose_name='家族'),
        ),
        migrations.AddField(
            model_name='familyarticle',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='familyarticles_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='familyarticle',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='core.Family', verbose_name='家族'),
        ),
        migrations.AddField(
            model_name='family',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='familys_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='family',
            name='messages',
            field=models.ManyToManyField(related_name='families', to='django_base.Message', verbose_name='家族消息'),
        ),
        migrations.AddField(
            model_name='family',
            name='users',
            field=models.ManyToManyField(related_name='families', through='core.FamilyMember', to=settings.AUTH_USER_MODEL, verbose_name='家族成员'),
        ),
        migrations.AddField(
            model_name='dailycheckinlog',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dailycheckinlogs_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='dailycheckinlog',
            name='prize_star_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.CreditStarTransaction', verbose_name='奖励星星流水记录'),
        ),
        migrations.AddField(
            model_name='creditstartransaction',
            name='user_credit',
            field=models.ForeignKey(blank=True, help_text='即余额减少的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditstartransactions_credit', to=settings.AUTH_USER_MODEL, verbose_name='贷方用户'),
        ),
        migrations.AddField(
            model_name='creditstartransaction',
            name='user_debit',
            field=models.ForeignKey(blank=True, help_text='即余额增加的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditstartransactions_debit', to=settings.AUTH_USER_MODEL, verbose_name='借方用户'),
        ),
        migrations.AddField(
            model_name='creditstarindextransaction',
            name='user_credit',
            field=models.ForeignKey(blank=True, help_text='即余额减少的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditstarindextransactions_credit', to=settings.AUTH_USER_MODEL, verbose_name='贷方用户'),
        ),
        migrations.AddField(
            model_name='creditstarindextransaction',
            name='user_debit',
            field=models.ForeignKey(blank=True, help_text='即余额增加的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditstarindextransactions_debit', to=settings.AUTH_USER_MODEL, verbose_name='借方用户'),
        ),
        migrations.AddField(
            model_name='creditdiamondtransaction',
            name='user_credit',
            field=models.ForeignKey(blank=True, help_text='即余额减少的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditdiamondtransactions_credit', to=settings.AUTH_USER_MODEL, verbose_name='贷方用户'),
        ),
        migrations.AddField(
            model_name='creditdiamondtransaction',
            name='user_debit',
            field=models.ForeignKey(blank=True, help_text='即余额增加的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditdiamondtransactions_debit', to=settings.AUTH_USER_MODEL, verbose_name='借方用户'),
        ),
        migrations.AddField(
            model_name='creditcointransaction',
            name='user_credit',
            field=models.ForeignKey(blank=True, help_text='即余额减少的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditcointransactions_credit', to=settings.AUTH_USER_MODEL, verbose_name='贷方用户'),
        ),
        migrations.AddField(
            model_name='creditcointransaction',
            name='user_debit',
            field=models.ForeignKey(blank=True, help_text='即余额增加的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditcointransactions_debit', to=settings.AUTH_USER_MODEL, verbose_name='借方用户'),
        ),
        migrations.AddField(
            model_name='badge',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='badges_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
