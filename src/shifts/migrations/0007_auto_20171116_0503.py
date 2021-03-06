# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0006_auto_20171109_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shifts',
            name='shift_date',
        ),
        migrations.AddField(
            model_name='shifts',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shifts',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='runs',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs_related', to='shifts.Shifts'),
        ),
    ]
