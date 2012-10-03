# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'PhotoSet.meta_descriptions'
        db.delete_column('gallery_photoset', 'meta_descriptions')

        # Adding field 'PhotoSet.meta_description'
        db.add_column('gallery_photoset', 'meta_description', self.gf('django.db.models.fields.TextField')(default='', max_length=250), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'PhotoSet.meta_descriptions'
        raise RuntimeError("Cannot reverse this migration. 'PhotoSet.meta_descriptions' and its values cannot be restored.")

        # Deleting field 'PhotoSet.meta_description'
        db.delete_column('gallery_photoset', 'meta_description')


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
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']
