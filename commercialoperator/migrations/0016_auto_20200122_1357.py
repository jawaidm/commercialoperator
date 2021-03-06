# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-22 05:57
from __future__ import unicode_literals

import commercialoperator.components.approvals.models
import commercialoperator.components.compliances.models
import commercialoperator.components.organisations.models
import commercialoperator.components.proposals.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0015_merge_20191217_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvaldocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.approvals.models.update_approval_doc_filename),
        ),
        migrations.AlterField(
            model_name='approvaldocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='approvallogdocument',
            name='_file',
            field=models.FileField(max_length=512, null=True, upload_to=commercialoperator.components.approvals.models.update_approval_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='approvallogdocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='compliancelogdocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.compliances.models.update_compliance_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='compliancelogdocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='onholddocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_onhold_doc_filename),
        ),
        migrations.AlterField(
            model_name='onholddocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='organisationlogdocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.organisations.models.update_organisation_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='organisationlogdocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='organisationrequest',
            name='identification',
            field=models.FileField(blank=True, max_length=512, null=True, upload_to='organisation/requests/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='organisationrequestlogdocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.organisations.models.update_organisation_request_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='organisationrequestlogdocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='proposaldocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_proposal_doc_filename),
        ),
        migrations.AlterField(
            model_name='proposaldocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='proposallogdocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_proposal_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='proposallogdocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='proposalrequireddocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_proposal_required_doc_filename),
        ),
        migrations.AlterField(
            model_name='proposalrequireddocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='qaofficerdocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_qaofficer_doc_filename),
        ),
        migrations.AlterField(
            model_name='qaofficerdocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='referraldocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_referral_doc_filename),
        ),
        migrations.AlterField(
            model_name='referraldocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='requirementdocument',
            name='_file',
            field=models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_requirement_doc_filename),
        ),
        migrations.AlterField(
            model_name='requirementdocument',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
    ]
