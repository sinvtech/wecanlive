# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 17:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0022_auto_20170712_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrizeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='金额')),
                ('remark', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='core.Prize', verbose_name='礼物')),
                ('user_credit', models.ForeignKey(blank=True, help_text='即余额减少的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prizetransactions_credit', to=settings.AUTH_USER_MODEL, verbose_name='贷方用户')),
                ('user_debit', models.ForeignKey(blank=True, help_text='即余额增加的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prizetransactions_debit', to=settings.AUTH_USER_MODEL, verbose_name='借方用户')),
            ],
            options={
                'verbose_name_plural': '礼物记录',
                'db_table': 'core_prize_transaction',
                'verbose_name': '礼物记录',
            },
        ),
        migrations.RemoveField(
            model_name='prizetransition',
            name='prize',
        ),
        migrations.RemoveField(
            model_name='prizetransition',
            name='user_credit',
        ),
        migrations.RemoveField(
            model_name='prizetransition',
            name='user_debit',
        ),
        migrations.RemoveField(
            model_name='prizeorder',
            name='coin_transition',
        ),
        migrations.RemoveField(
            model_name='prizeorder',
            name='diamond_transition',
        ),
        migrations.RemoveField(
            model_name='prizeorder',
            name='prize_transition',
        ),
        migrations.AddField(
            model_name='prizeorder',
            name='coin_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prize_orders', to='core.CreditCoinTransaction', verbose_name='金幣消費记录'),
        ),
        migrations.AddField(
            model_name='prizeorder',
            name='diamond_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prize_orders', to='core.CreditDiamondTransaction', verbose_name='主播鑽石记录'),
        ),
        migrations.AddField(
            model_name='prizeorder',
            name='star_index_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prize_orders', to='core.CreditStarIndexTransaction', verbose_name='主播元气记录'),
        ),
        migrations.DeleteModel(
            name='PrizeTransition',
        ),
        migrations.AddField(
            model_name='prizeorder',
            name='prize_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prize_orders', to='core.PrizeTransaction', verbose_name='礼物记录'),
        ),
    ]