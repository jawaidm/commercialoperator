# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-06-03 08:42
from __future__ import unicode_literals

import commercialoperator.components.bookings.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commercialoperator', '0020_auto_20200207_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFeeDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(choices=[(0, 'Discount application'), (1, 'Discount licence')], max_length=40)),
                ('discount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reset_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='organisation',
            name='application_discount',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='organisation',
            name='apply_application_discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organisation',
            name='apply_licence_discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organisation',
            name='licence_discount',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='applicationfee',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='applicationfee',
            name='expiry_time',
            field=models.DateTimeField(blank=True, default=commercialoperator.components.bookings.models.expiry_time, null=True),
        ),
        migrations.AlterField(
            model_name='applicationfee',
            name='payment_type',
            field=models.SmallIntegerField(choices=[(0, 'Internet booking'), (1, 'Reception booking'), (2, 'Black booking'), (3, 'Temporary reservation'), (4, 'No payment')], default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='expiry_time',
            field=models.DateTimeField(blank=True, default=commercialoperator.components.bookings.models.expiry_time, null=True),
        ),
        migrations.AlterField(
            model_name='parkbooking',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='previous_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commercialoperator.Proposal'),
        ),
        migrations.AddField(
            model_name='applicationfeediscount',
            name='proposal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fee_discounts', to='commercialoperator.Proposal'),
        ),
        migrations.AddField(
            model_name='applicationfeediscount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_by_fee_discount', to=settings.AUTH_USER_MODEL),
        ),
    ]
