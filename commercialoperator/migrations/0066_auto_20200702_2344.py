# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-02 15:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commercialoperator', '0065_auto_20200702_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmingFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_invoice', models.BooleanField(default=False)),
                ('confirmation_sent', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiry_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_type', models.SmallIntegerField(choices=[(0, 'Internet booking'), (1, 'Reception booking'), (2, 'Black booking'), (3, 'Temporary reservation')], default=0)),
                ('cost', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('deferred_payment_date', models.DateField(blank=True, null=True)),
                ('payment_due_notification_sent', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by_filming_fee', to=settings.AUTH_USER_MODEL)),
                ('proposal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='filming_fees', to='commercialoperator.Compliance')),
            ],
        ),
        migrations.CreateModel(
            name='FilmingFeeInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_reference', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('filming_fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filming_fee_invoices', to='commercialoperator.FilmingFee')),
            ],
        ),
        migrations.AlterField(
            model_name='proposaltype',
            name='name',
            field=models.CharField(choices=[('T Class', 'T Class'), ('Event', 'Event'), ('Filming', 'Filming')], default='T Class', max_length=64, verbose_name='Application name (eg. T Class, Filming, Event, E Class)'),
        ),
    ]
