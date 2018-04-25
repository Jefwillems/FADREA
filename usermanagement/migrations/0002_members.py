# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=64)),
                ('last_name', models.CharField(default='', max_length=64)),
                ('email', models.EmailField(default='info@fadrea.be', max_length=128)),
            ],
        ),
    ]
