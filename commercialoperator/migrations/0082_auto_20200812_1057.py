# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-08-12 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0081_auto_20200812_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsettings',
            name='key',
            field=models.CharField(choices=[('credit_facility_link', 'Credit Facility Link'), ('deed_poll', 'Deed poll'), ('online_training_document', 'Online Training Document'), ('park_finder_link', 'Park Finder Link'), ('fees_and_charges', 'Fees and charges link'), ('commercial_filming_handbook', 'Commercial Filming Handbook link'), ('park_stay_link', 'Park Stay Link')], max_length=255),
        ),
    ]
