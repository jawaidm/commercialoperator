# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-04 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0046_auto_20200501_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposaleventactivities',
            name='event_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Event name'),
        ),
    ]
