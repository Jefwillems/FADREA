# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-30 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotlight',
            name='left_title',
            field=models.CharField(blank=True, default='', max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='right_title',
            field=models.CharField(blank=True, default='', max_length=24, null=True),
        ),
    ]