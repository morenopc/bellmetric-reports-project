# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    class Meta:
        db_table = 'company'


class Campaign(models.Model):
    id = models.BigIntegerField(primary_key=True)
    company = models.ForeignKey('Company')
    name = models.CharField(max_length=255, unique=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    retention = models.TextField() # This field type is a guess.
    max_allocated_numbers = models.IntegerField(null=True, blank=True)
    domain_name = models.CharField(max_length=255, blank=True)
    ga_account_id = models.CharField(max_length=20, blank=True)
    enabled = models.BooleanField()
    sc_trackingserver = models.CharField(max_length=255, blank=True)
    sc_reportsuite_id = models.CharField(max_length=255, blank=True)
    sc_value_event = models.CharField(max_length=255, blank=True)
    sc_duration_evar = models.CharField(max_length=255, blank=True)
    sc_call_event = models.CharField(max_length=255, blank=True)
    sc_pagename_evar = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'campaign'


class SourceType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    source_type = models.CharField(max_length=255, unique=True)
    class Meta:
        db_table = 'source_type'


class Source(models.Model):
    id = models.BigIntegerField(primary_key=True)
    visitor_id = models.BigIntegerField()
    time = models.DateTimeField()
    source_type = models.ForeignKey('SourceType', null=True, blank=True)
    url = models.TextField(blank=True)
    class Meta:
        db_table = 'source'


class Cdr(models.Model):
    id = models.BigIntegerField(primary_key=True)
    call_start = models.DateTimeField(null=True, blank=True)
    campaign = models.ForeignKey(Campaign, null=True, blank=True)
    caller = models.CharField(max_length=255, blank=True)
    called = models.CharField(max_length=255, blank=True)
    call_duration = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'cdr'


class CdrSource(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cdr = models.ForeignKey(Cdr)
    source = models.ForeignKey('Source')
    class Meta:
        db_table = 'cdr_source'
