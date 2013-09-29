# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ProjectScore'
        db.delete_table(u'project_projectscore')

        # Deleting model 'ProjectScoreAttribute'
        db.delete_table(u'project_projectscoreattribute')

        # Deleting model 'ScoreAttribute'
        db.delete_table(u'project_scoreattribute')

    def backwards(self, orm):
        # Adding model 'ProjectScore'
        db.create_table(u'project_projectscore', (
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(
                auto_now=True, blank=True)),
            ('total_score', self.gf('django.db.models.fields.DecimalField')(
                max_digits=8, decimal_places=2)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['project.Project'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(
                auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(
                primary_key=True)),
        ))
        db.send_create_signal(u'project', ['ProjectScore'])

        # Adding model 'ProjectScoreAttribute'
        db.create_table(u'project_projectscoreattribute', (
            ('project_score',
             self.gf('django.db.models.fields.related.ForeignKey')(
                 to=orm['project.ProjectScore'])),
            ('score_value', self.gf('django.db.models.fields.DecimalField')(
                max_digits=8, decimal_places=2)),
            ('score_attribute',
             self.gf('django.db.models.fields.related.ForeignKey')(
                 to=orm['project.ScoreAttribute'])),
            ('result', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(
                primary_key=True)),
        ))
        db.send_create_signal(u'project', ['ProjectScoreAttribute'])

        # Adding model 'ScoreAttribute'
        db.create_table(u'project_scoreattribute', (
            ('slug', self.gf('django.db.models.fields.SlugField')(
                max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(
                max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(
                primary_key=True)),
        ))
        db.send_create_signal(u'project', ['ScoreAttribute'])

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
                         {'max_length': '200'})
        }
    }

    complete_apps = ['project']
