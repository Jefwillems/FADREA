# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-28 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180428_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
