# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shifts',
            name='pub_date',
        ),
    ]
