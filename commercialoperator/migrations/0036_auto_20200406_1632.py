# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-04-06 08:32
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0035_districtproposaldeclineddetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lodgement_number', models.CharField(blank=True, default='', max_length=9)),
                ('status', models.CharField(choices=[('current', 'Current'), ('expired', 'Expired'), ('cancelled', 'Cancelled'), ('surrendered', 'Surrendered'), ('suspended', 'Suspended'), ('extended', 'extended')], default='current', max_length=40)),
                ('renewal_sent', models.BooleanField(default=False)),
                ('issue_date', models.DateTimeField()),
                ('original_issue_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('surrender_details', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('suspension_details', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('extracted_fields', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('cancellation_details', models.TextField(blank=True)),
                ('extend_details', models.TextField(blank=True)),
                ('cancellation_date', models.DateField(blank=True, null=True)),
                ('set_to_cancel', models.BooleanField(default=False)),
                ('set_to_suspend', models.BooleanField(default=False)),
                ('set_to_surrender', models.BooleanField(default=False)),
                ('renewal_count', models.PositiveSmallIntegerField(default=0, verbose_name='Number of times an Approval has been renewed')),
                ('migrated', models.BooleanField(default=False)),
                ('current_district_proposal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_approvals', to='commercialoperator.DistrictProposal')),
                ('replaced_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commercialoperator.DistrictApproval')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='districtapproval',
            unique_together=set([('lodgement_number', 'issue_date')]),
        ),
    ]
