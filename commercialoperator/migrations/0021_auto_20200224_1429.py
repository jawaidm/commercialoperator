# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-24 06:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0020_auto_20200207_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalFilmingAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalFilmingActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_title', models.CharField(max_length=100, verbose_name='Activity title')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalFilmingEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cameras', models.TextField(blank=True, null=True, verbose_name='Number and type of cameras to be used')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalFilmingOtherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety_details', models.TextField(blank=True, null=True, verbose_name='Steps taken to ensure safety of others')),
                ('camping_fee_waived', models.BooleanField(default=False)),
                ('fee_waived_num_people', models.SmallIntegerField(blank=True, null=True, verbose_name='For how many people')),
                ('insurance_expiry', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='proposal',
            name='previous_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commercialoperator.Proposal'),
        ),
        migrations.AlterField(
            model_name='proposaltype',
            name='name',
            field=models.CharField(choices=[('T Class', 'T Class'), ('Event', 'Event'), ('Filming', 'Filming')], default='T Class', max_length=64, verbose_name='Application name (eg. T Class, Filming, Event, E Class)'),
        ),
        migrations.AddField(
            model_name='proposalfilmingotherdetails',
            name='proposal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filming_other_details', to='commercialoperator.Proposal'),
        ),
        migrations.AddField(
            model_name='proposalfilmingequipment',
            name='proposal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filming_equipment', to='commercialoperator.Proposal'),
        ),
        migrations.AddField(
            model_name='proposalfilmingactivity',
            name='proposal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filming_activity', to='commercialoperator.Proposal'),
        ),
        migrations.AddField(
            model_name='proposalfilmingaccess',
            name='proposal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filming_access', to='commercialoperator.Proposal'),
        ),
    ]
