# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-28 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180428_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotlight',
            name='left_title',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='spotlight',
            name='right_title',
            field=models.CharField(default='', max_length=32),
        ),
    ]
