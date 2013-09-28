# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'project_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('repo_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'project', ['Project'])

        # Adding model 'ProjectScore'
        db.create_table(u'project_projectscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('total_score', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'project', ['ProjectScore'])

        # Adding model 'ScoreAttribute'
        db.create_table(u'project_scoreattribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'project', ['ScoreAttribute'])

        # Adding model 'ProjectScoreAttribute'
        db.create_table(u'project_projectscoreattribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score_attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ScoreAttribute'])),
            ('project_score', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ProjectScore'])),
            ('score_value', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('result', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'project', ['ProjectScoreAttribute'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'project_project')

        # Deleting model 'ProjectScore'
        db.delete_table(u'project_projectscore')

        # Deleting model 'ScoreAttribute'
        db.delete_table(u'project_scoreattribute')

        # Deleting model 'ProjectScoreAttribute'
        db.delete_table(u'project_projectscoreattribute')


    models = {
        u'project.project': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Project'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'repo_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'project.projectscore': {
            'Meta': {'object_name': 'ProjectScore'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'total_score': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        u'project.projectscoreattribute': {
            'Meta': {'object_name': 'ProjectScoreAttribute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_score': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.ProjectScore']"}),
            'result': ('django.db.models.fields.TextField', [], {}),
            'score_attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.ScoreAttribute']"}),
            'score_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        u'project.scoreattribute': {
            'Meta': {'object_name': 'ScoreAttribute'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['project']