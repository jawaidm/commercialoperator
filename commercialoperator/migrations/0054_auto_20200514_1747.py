# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-14 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0053_auto_20200514_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='filming_approval_type',
            field=models.CharField(choices=[('lawful_authority', 'Lawful Authority'), ('licence', 'Licence')], default='licence', max_length=30, verbose_name='Filming Approval Type'),
        ),
    ]
