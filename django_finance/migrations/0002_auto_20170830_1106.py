# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-30 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrecord',
            name='product_id',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='产品编号'),
        ),
        migrations.AlterField(
            model_name='paymentrecord',
            name='platform',
            field=models.CharField(blank=True, choices=[('BALANCE', '余额支付'), ('ALIPAY', '支付宝'), ('WXPAY', '微信支付'), ('APP', 'Buy in app'), ('PAYPAL', 'Paypal'), ('OTHER', '其他')], default='', max_length=20, verbose_name='支付平台'),
        ),
    ]
