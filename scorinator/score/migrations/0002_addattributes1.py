# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        sa1 = orm.ScoreAttribute()
        sa1.name = "Readme present"
        sa1.description = "Does it have a ReadMe file"
        sa1.slug = 'has_readme'
        sa1.save()

        sa2 = orm.ScoreAttribute()
        sa2.name = "License file"
        sa2.description = "Does it have a License file"
        sa2.slug = 'has_license'
        sa2.save()

        sa3 = orm.ScoreAttribute()
        sa3.name = "Repo stars"
        sa3.description = "How many stars does it have"
        sa3.slug = 'repo_stars'
        sa3.save()

        sa4 = orm.ScoreAttribute()
        sa4.name = "Repo watchers"
        sa4.description = "How many watchers does it have"
        sa4.slug = 'repo_watchers'
        sa4.save()

        sa5 = orm.ScoreAttribute()
        sa5.name = "Repo commits"
        sa5.description = "How many commits does it have"
        sa5.slug = 'repo_commits'
        sa5.save()

        sa6 = orm.ScoreAttribute()
        sa6.name = "Repo last commit"
        sa6.description = "How many days since last commit"
        sa6.slug = 'repo_last_commit_days'
        sa6.save()

        sa7 = orm.ScoreAttribute()
        sa7.name = "Repo commiters"
        sa7.description = "How many commiters does project have"
        sa7.slug = 'repo_commiters'
        sa7.save()

        sa8 = orm.ScoreAttribute()
        sa8.name = "Repo Pull requests"
        sa8.description = "How many pull requests does project have"
        sa8.slug = 'repo_pullrequests'
        sa8.save()

        sa9 = orm.ScoreAttribute()
        sa9.name = "project releases"
        sa9.description = "How many releases does project have"
        sa9.slug = 'project_releases'
        sa9.save()

        sa10 = orm.ScoreAttribute()
        sa10.name = "Repo forks"
        sa10.description = "How many forks does project have"
        sa10.slug = 'repo_forks'
        sa10.save()

        sa11 = orm.ScoreAttribute()
        sa11.name = "Travis CI"
        sa11.description = "Does project use Travis CI"
        sa11.slug = 'has_travisci'
        sa11.save()

        sa12 = orm.ScoreAttribute()
        sa12.name = "Coveralls"
        sa12.description = "Does project use Coveralls"
        sa12.slug = 'has_coveralls'
        sa12.save()

        sa13 = orm.ScoreAttribute()
        sa13.name = "Read the Docs"
        sa13.description = "Does project use Read the Docs"
        sa13.slug = 'has_readthedocs'
        sa13.save()

        sa14 = orm.ScoreAttribute()
        sa14.name = "Unit tests"
        sa14.description = "Does project have unit tests"
        sa14.slug = 'has_unittests'
        sa14.save()

        sa15 = orm.ScoreAttribute()
        sa15.name = "Test Coverage"
        sa15.description = "What is the unit test Coverage for project"
        sa15.slug = 'test_coverage'
        sa15.save()

    def backwards(self, orm):
        "Write your backwards methods here."

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
                            {'max_digits': '8', 'decimal_places': '2'})
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
                            {'max_digits': '8', 'decimal_places': '2'})
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
    symmetrical = True
