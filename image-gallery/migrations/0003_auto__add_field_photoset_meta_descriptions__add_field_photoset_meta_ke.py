# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'PhotoSet.meta_descriptions'
        db.add_column('gallery_photoset', 'meta_descriptions', self.gf('django.db.models.fields.TextField')(default='', max_length=250), keep_default=False)

        # Adding field 'PhotoSet.meta_keywords'
        db.add_column('gallery_photoset', 'meta_keywords', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'PhotoSet.meta_descriptions'
        db.delete_column('gallery_photoset', 'meta_descriptions')

        # Deleting field 'PhotoSet.meta_keywords'
        db.delete_column('gallery_photoset', 'meta_keywords')


    models = {
        'gallery.photo': {
            'Meta': {'ordering': "['sort_order', 'created']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'photoset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.PhotoSet']"}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '100'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'gallery.photoset': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'PhotoSet'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_descriptions': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']
