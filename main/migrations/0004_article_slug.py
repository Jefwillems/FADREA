# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-23 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]