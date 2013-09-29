# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ProjectScoreAttribute.score_value'
        db.alter_column(u'score_projectscoreattribute', 'score_value',
                        self.gf('django.db.models.fields.DecimalField')(
                            null=True, max_digits=8, decimal_places=2))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for
        # 'ProjectScoreAttribute.score_value'
        raise RuntimeError(
            "Cannot reverse this migration. 'ProjectScoreAttribute.score_value"
            "' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct
        # migration
        # Changing field 'ProjectScoreAttribute.score_value'
        db.alter_column(u'score_projectscoreattribute', 'score_value',
                        self.gf('django.db.models.fields.DecimalField')(
                            max_digits=8, decimal_places=2))

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
        },
        u'score.projectscore': {
            'Meta': {'ordering': "('total_score',)",
                     'object_name': 'ProjectScore'},
            'date_added': ('django.db.models.fields.DateTimeField', [],
                           {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [],
                             {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [],
                        {'to': u"orm['project.Project']"}),
            'total_score': ('django.db.models.fields.DecimalField', [],
                            {'default': 'None',
                             'null': 'True',
                             'max_digits': '8',
                             'decimal_places': '2', 'blank': 'True'})
        },
        u'score.projectscoreattribute': {
            'Meta': {'object_name': 'ProjectScoreAttribute'},
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'project_score': ('django.db.models.fields.related.ForeignKey', [],
                              {'to': u"orm['score.ProjectScore']"}),
            'result': ('django.db.models.fields.TextField', [], {}),
            'score_attribute': ('django.db.models.fields.related.ForeignKey',
                                [], {'to': u"orm['score.ScoreAttribute']"}),
            'score_value': ('django.db.models.fields.DecimalField', [],
                            {'default': 'None',
                             'null': 'True',
                             'max_digits': '8',
                             'decimal_places': '2',
                             'blank': 'True'})
        },
        u'score.scoreattribute': {
            'Meta': {'object_name': 'ScoreAttribute'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [],
                     {'max_length': '50'})
        }
    }

    complete_apps = ['score']
