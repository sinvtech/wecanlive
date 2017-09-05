# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-04 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_activityparticipation_badge_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityparticipation',
            name='fifth_diamond_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fifth_activity_participation', to='core.CreditDiamondTransaction', verbose_name='第五阶段钻石奖励记录'),
        ),
        migrations.AddField(
            model_name='activityparticipation',
            name='fourth_diamond_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth_activity_participation', to='core.CreditDiamondTransaction', verbose_name='第四阶段钻石奖励记录'),
        ),
        migrations.AddField(
            model_name='activityparticipation',
            name='second_diamond_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_activity_participation', to='core.CreditDiamondTransaction', verbose_name='第二阶段钻石奖励记录'),
        ),
        migrations.AddField(
            model_name='activityparticipation',
            name='third_diamond_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_activity_participation', to='core.CreditDiamondTransaction', verbose_name='第三阶段钻石奖励记录'),
        ),
    ]