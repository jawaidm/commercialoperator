# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-08-06 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistquestion',
            name='answer_type',
            field=models.CharField(choices=[('yes_no', 'Yes/No type'), ('free_text', 'Free text type')], default='yes_no', max_length=30, verbose_name='Answer type'),
        ),
    ]
