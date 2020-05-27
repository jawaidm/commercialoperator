# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-25 05:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0022_auto_20200525_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationfeediscount',
            name='discount',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]