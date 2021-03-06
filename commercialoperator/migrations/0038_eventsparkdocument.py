# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-04-09 02:40
from __future__ import unicode_literals

import commercialoperator.components.proposals.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0037_auto_20200409_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsParkDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('_file', models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_events_park_doc_filename)),
                ('input_name', models.CharField(blank=True, max_length=255, null=True)),
                ('can_delete', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
                ('events_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_park_documents', to='commercialoperator.ProposalEventsParks')),
            ],
        ),
    ]
