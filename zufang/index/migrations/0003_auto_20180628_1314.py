# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-28 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180625_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='url',
            field=models.CharField(max_length=500, verbose_name='网址'),
        ),
    ]
