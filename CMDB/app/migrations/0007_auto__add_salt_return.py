# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'salt_return'
        db.create_table(u'app_salt_return', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fun', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('jid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('result', self.gf('django.db.models.fields.TextField')()),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('success', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('full_ret', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'app', ['salt_return'])


    def backwards(self, orm):
        # Deleting model 'salt_return'
        db.delete_table(u'app_salt_return')


    models = {
        u'app.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'app.hostlist': {
            'Meta': {'object_name': 'HostList'},
            'application': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bianhao': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['app.Group']", 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'unique': 'True', 'max_length': '15'})
        },
        u'app.idc': {
            'Meta': {'object_name': 'Idc'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'app.salt_return': {
            'Meta': {'object_name': 'salt_return'},
            'full_ret': ('django.db.models.fields.TextField', [], {}),
            'fun': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'result': ('django.db.models.fields.TextField', [], {}),
            'success': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'app.serverasset': {
            'Meta': {'object_name': 'ServerAsset'},
            'cpu_groups': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'cpu_model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cpu_nums': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'disk': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mem': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'productname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'service_tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'app.upload': {
            'Meta': {'object_name': 'Upload'},
            'headImg': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']