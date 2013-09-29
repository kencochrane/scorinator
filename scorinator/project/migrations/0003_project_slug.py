# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.slug'
        db.add_column(u'project_project', 'slug',
                      self.gf('django.db.models.fields.SlugField')(
                          default='empty', unique=True, max_length=50),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Project.slug'
        db.delete_column(u'project_project', 'slug')

    models = {
        u'project.project': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Project'},
            'date_added': ('django.db.models.fields.DateTimeField', [],
                           {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [],
                             {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'max_length': '150'}),
            'repo_url': ('django.db.models.fields.URLField', [],
                         {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [],
                     {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['project']
