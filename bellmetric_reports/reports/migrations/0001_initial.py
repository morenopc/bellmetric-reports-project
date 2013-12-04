# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'company', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'reports', ['Company'])

        # Adding model 'Campaign'
        db.create_table(u'campaign', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('retention', self.gf('django.db.models.fields.TextField')()),
            ('max_allocated_numbers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('domain_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ga_account_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sc_trackingserver', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sc_reportsuite_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sc_value_event', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sc_duration_evar', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sc_call_event', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sc_pagename_evar', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'reports', ['Campaign'])

        # Adding model 'SourceType'
        db.create_table(u'source_type', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('source_type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'reports', ['SourceType'])

        # Adding model 'Source'
        db.create_table(u'source', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('visitor_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('source_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.SourceType'], null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'reports', ['Source'])

        # Adding model 'Cdr'
        db.create_table(u'cdr', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('call_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Campaign'], null=True, blank=True)),
            ('caller', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('called', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('call_duration', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Cdr'])

        # Adding model 'CdrSource'
        db.create_table(u'cdr_source', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('cdr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Cdr'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Source'])),
        ))
        db.send_create_signal(u'reports', ['CdrSource'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'company')

        # Deleting model 'Campaign'
        db.delete_table(u'campaign')

        # Deleting model 'SourceType'
        db.delete_table(u'source_type')

        # Deleting model 'Source'
        db.delete_table(u'source')

        # Deleting model 'Cdr'
        db.delete_table(u'cdr')

        # Deleting model 'CdrSource'
        db.delete_table(u'cdr_source')


    models = {
        u'reports.campaign': {
            'Meta': {'object_name': 'Campaign', 'db_table': "u'campaign'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'domain_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ga_account_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'max_allocated_numbers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'retention': ('django.db.models.fields.TextField', [], {}),
            'sc_call_event': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sc_duration_evar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sc_pagename_evar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sc_reportsuite_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sc_trackingserver': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sc_value_event': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reports.cdr': {
            'Meta': {'object_name': 'Cdr', 'db_table': "u'cdr'"},
            'call_duration': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'call_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'called': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'caller': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Campaign']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'reports.cdrsource': {
            'Meta': {'object_name': 'CdrSource', 'db_table': "u'cdr_source'"},
            'cdr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Cdr']"}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Source']"})
        },
        u'reports.company': {
            'Meta': {'object_name': 'Company', 'db_table': "u'company'"},
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'reports.source': {
            'Meta': {'object_name': 'Source', 'db_table': "u'source'"},
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'source_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.SourceType']", 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'visitor_id': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'reports.sourcetype': {
            'Meta': {'object_name': 'SourceType', 'db_table': "u'source_type'"},
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'source_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['reports']