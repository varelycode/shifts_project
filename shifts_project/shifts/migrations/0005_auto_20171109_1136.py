# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 19:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0004_auto_20171109_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shifts',
            old_name='shift_date',
            new_name='shift_start',
        ),
    ]
