# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 09:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('content', models.CharField(max_length=255, verbose_name='详细地址')),
                ('receiver', models.CharField(max_length=50, verbose_name='收件人')),
                ('mobile', models.CharField(max_length=20, verbose_name='联系电话')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberaddresss_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '地址',
                'db_table': 'member_address',
                'verbose_name': '地址',
            },
        ),
        migrations.CreateModel(
            name='OAuthEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(blank=True, choices=[('WECHAT_APP', '微信APP'), ('WECHAT_BIZ', '微信公众平台'), ('ALIPAY', '支付宝'), ('QQ', 'QQ'), ('WEIBO', '微博')], default='', max_length=20, verbose_name='第三方平台')),
                ('app', models.CharField(blank=True, default='', max_length=120, verbose_name='app')),
                ('openid', models.CharField(max_length=128, verbose_name='用户OpenID')),
                ('nickname', models.CharField(max_length=128, null=True, verbose_name='用户昵称')),
                ('headimgurl', models.URLField(blank=True, null=True, verbose_name='用户头像')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='oauth/avatar/', verbose_name='头像文件')),
                ('params', models.TextField(blank=True, default='', verbose_name='params')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oauthentrys_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '第三方授权',
                'db_table': 'member_oauth_entry',
                'verbose_name': '第三方授权',
            },
        ),
        migrations.AlterUniqueTogether(
            name='oauthentry',
            unique_together=set([('app', 'openid')]),
        ),
    ]
