# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0009_auto_20171116_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='user_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
