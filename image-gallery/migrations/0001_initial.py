# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PhotoSet'
        db.create_table('gallery_photoset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('sort_order', self.gf('django.db.models.fields.FloatField')(default=100)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['PhotoSet'])

        # Adding model 'Photo'
        db.create_table('gallery_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('photoset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.PhotoSet'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.FloatField')(default=100)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['Photo'])


    def backwards(self, orm):
        
        # Deleting model 'PhotoSet'
        db.delete_table('gallery_photoset')

        # Deleting model 'Photo'
        db.delete_table('gallery_photo')


    models = {
        'gallery.photo': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Photo'},
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']
