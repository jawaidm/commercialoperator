# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-03 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0067_auto_20200703_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposalfilmingactivity',
            name='half_day',
            field=models.BooleanField(default=False, verbose_name='Filming full day or half day'),
        ),
    ]