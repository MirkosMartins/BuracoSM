# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tipo'
        db.create_table(u'eventos_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'eventos', ['Tipo'])

        # Adding model 'Evento'
        db.create_table(u'eventos_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Tipo'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('posicao', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'eventos', ['Evento'])


    def backwards(self, orm):
        # Deleting model 'Tipo'
        db.delete_table(u'eventos_tipo')

        # Deleting model 'Evento'
        db.delete_table(u'eventos_evento')


    models = {
        u'eventos.evento': {
            'Meta': {'ordering': "['-id', 'titulo']", 'object_name': 'Evento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posicao': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Tipo']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'eventos.tipo': {
            'Meta': {'object_name': 'Tipo'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['eventos']