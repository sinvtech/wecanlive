# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-14 17:17
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
            name='AccountTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='金额')),
                ('remark', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
                ('type', models.CharField(blank=True, choices=[('RECHARGE', '充值'), ('WITHDRAW', '提现'), ('COMMISSION', '佣金'), ('PURCHASE', '消费'), ('FEE', '手续费'), ('REFUND', '退款'), ('DIRECT_PAY', '直接支付')], default='', max_length=20, verbose_name='流水类型')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='django_finance.AccountTransaction', verbose_name='上级')),
                ('user_credit', models.ForeignKey(blank=True, help_text='即余额减少的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounttransactions_credit', to=settings.AUTH_USER_MODEL, verbose_name='贷方用户')),
                ('user_debit', models.ForeignKey(blank=True, help_text='即余额增加的用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounttransactions_debit', to=settings.AUTH_USER_MODEL, verbose_name='借方用户')),
            ],
            options={
                'verbose_name_plural': '财务流水',
                'db_table': 'core_finance_account_transaction',
                'verbose_name': '财务流水',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('code', models.CharField(max_length=20, verbose_name='银行编码')),
                ('pinyin', models.CharField(max_length=100, verbose_name='银行名称拼音')),
            ],
            options={
                'verbose_name_plural': '银行',
                'db_table': 'core_finance_bank',
                'verbose_name': '银行',
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('holder_name', models.CharField(max_length=40, verbose_name='开户人')),
                ('number', models.CharField(max_length=50, unique=True, verbose_name='账号')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccounts_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='django_finance.Bank', verbose_name='开户行')),
            ],
            options={
                'verbose_name_plural': '用户账号',
                'db_table': 'core_finance_bank_account',
                'verbose_name': '用户账号',
            },
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(blank=True, choices=[('BALANCE', '余额支付'), ('ALIPAY', '支付宝'), ('WXPAY', '微信支付'), ('APP', 'Buy in app'), ('PAYPAL', 'Paypal')], default='', max_length=20, verbose_name='支付平台')),
                ('out_trade_no', models.CharField(max_length=45, verbose_name='外部订单号')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='支付金额')),
                ('subject', models.CharField(max_length=255, verbose_name='订单标题')),
                ('description', models.CharField(blank=True, default='', max_length=255, verbose_name='订单内容')),
                ('status', models.CharField(blank=True, default='', max_length=45, verbose_name='订单状态')),
                ('seller_id', models.CharField(blank=True, default='', max_length=255, verbose_name='商户ID')),
                ('seller_email', models.CharField(blank=True, default='', max_length=255, verbose_name='商户email')),
                ('buyer_id', models.CharField(blank=True, default='', max_length=255, verbose_name='买家ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_notify', models.DateTimeField(blank=True, null=True, verbose_name='回调时间')),
                ('notify_data', models.TextField(blank=True, default='', verbose_name='完整回调数据')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paymentrecords_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('payment_transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_finance.AccountTransaction', verbose_name='支付产生余额增加的流水')),
            ],
            options={
                'verbose_name_plural': '支付记录',
                'db_table': 'core_finance_payment_record',
                'verbose_name': '支付记录',
            },
        ),
        migrations.CreateModel(
            name='RechargeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='充值金额')),
                ('account_transaction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recharge_record', to='django_finance.AccountTransaction', verbose_name='充值流水')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rechargerecords_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('payment_record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recharge_record', to='django_finance.PaymentRecord', verbose_name='支付记录')),
            ],
            options={
                'verbose_name_plural': '充值记录',
                'db_table': 'core_finance_recharge_record',
                'verbose_name': '充值记录',
            },
        ),
        migrations.CreateModel(
            name='WithdrawRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='名称')),
                ('is_del', models.BooleanField(default=False, verbose_name='已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('sorting', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.CharField(choices=[('PENDING', '申请中'), ('APPROVED', '提现成功'), ('REJECTED', '驳回')], default='PENDING', max_length=20, verbose_name='状态')),
                ('date_approve', models.DateTimeField(blank=True, null=True, verbose_name='审批时间')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='金额')),
                ('fee_rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, verbose_name='提现手续费率')),
                ('actual_amount', models.DecimalField(decimal_places=2, max_digits=18, null=True, verbose_name='实际金额')),
                ('account_transaction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withdraw_record', to='django_finance.AccountTransaction', verbose_name='提现流水')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withdrawrecords_owned', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdraw_records', to='django_finance.BankAccount', verbose_name='银行')),
                ('user_approve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='审核员')),
            ],
            options={
                'verbose_name_plural': '提现记录',
                'db_table': 'core_finance_withdraw_record',
                'verbose_name': '提现记录',
            },
        ),
    ]
