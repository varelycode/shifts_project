# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0010_run_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='shift',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='runs_related', to='shifts.Shift'),
        ),
    ]
