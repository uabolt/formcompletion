# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'ImageTask.correctAnswer2' to match new field type.
        db.rename_column(u'imagetask_imagetask', 'correctAnswer2', 'correctAnswer2_id')
        # Changing field 'ImageTask.correctAnswer2'
        db.alter_column(u'imagetask_imagetask', 'correctAnswer2_id', self.gf('django.db.models.fields.related.OneToOneField')(default='', unique=True, to=orm['imagetask.Image']))
        # Adding index on 'ImageTask', fields ['correctAnswer2']
        db.create_index(u'imagetask_imagetask', ['correctAnswer2_id'])

        # Adding unique constraint on 'ImageTask', fields ['correctAnswer2']
        db.create_unique(u'imagetask_imagetask', ['correctAnswer2_id'])


        # Renaming column for 'ImageTask.correctAnswer3' to match new field type.
        db.rename_column(u'imagetask_imagetask', 'correctAnswer3', 'correctAnswer3_id')
        # Changing field 'ImageTask.correctAnswer3'
        db.alter_column(u'imagetask_imagetask', 'correctAnswer3_id', self.gf('django.db.models.fields.related.OneToOneField')(default='', unique=True, to=orm['imagetask.Image']))
        # Adding index on 'ImageTask', fields ['correctAnswer3']
        db.create_index(u'imagetask_imagetask', ['correctAnswer3_id'])

        # Adding unique constraint on 'ImageTask', fields ['correctAnswer3']
        db.create_unique(u'imagetask_imagetask', ['correctAnswer3_id'])


        # Renaming column for 'ImageTask.correctAnswer1' to match new field type.
        db.rename_column(u'imagetask_imagetask', 'correctAnswer1', 'correctAnswer1_id')
        # Changing field 'ImageTask.correctAnswer1'
        db.alter_column(u'imagetask_imagetask', 'correctAnswer1_id', self.gf('django.db.models.fields.related.OneToOneField')(default='', unique=True, to=orm['imagetask.Image']))
        # Adding index on 'ImageTask', fields ['correctAnswer1']
        db.create_index(u'imagetask_imagetask', ['correctAnswer1_id'])

        # Adding unique constraint on 'ImageTask', fields ['correctAnswer1']
        db.create_unique(u'imagetask_imagetask', ['correctAnswer1_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ImageTask', fields ['correctAnswer1']
        db.delete_unique(u'imagetask_imagetask', ['correctAnswer1_id'])

        # Removing index on 'ImageTask', fields ['correctAnswer1']
        db.delete_index(u'imagetask_imagetask', ['correctAnswer1_id'])

        # Removing unique constraint on 'ImageTask', fields ['correctAnswer3']
        db.delete_unique(u'imagetask_imagetask', ['correctAnswer3_id'])

        # Removing index on 'ImageTask', fields ['correctAnswer3']
        db.delete_index(u'imagetask_imagetask', ['correctAnswer3_id'])

        # Removing unique constraint on 'ImageTask', fields ['correctAnswer2']
        db.delete_unique(u'imagetask_imagetask', ['correctAnswer2_id'])

        # Removing index on 'ImageTask', fields ['correctAnswer2']
        db.delete_index(u'imagetask_imagetask', ['correctAnswer2_id'])


        # Renaming column for 'ImageTask.correctAnswer2' to match new field type.
        db.rename_column(u'imagetask_imagetask', 'correctAnswer2_id', 'correctAnswer2')
        # Changing field 'ImageTask.correctAnswer2'
        db.alter_column(u'imagetask_imagetask', 'correctAnswer2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Renaming column for 'ImageTask.correctAnswer3' to match new field type.
        db.rename_column(u'imagetask_imagetask', 'correctAnswer3_id', 'correctAnswer3')
        # Changing field 'ImageTask.correctAnswer3'
        db.alter_column(u'imagetask_imagetask', 'correctAnswer3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Renaming column for 'ImageTask.correctAnswer1' to match new field type.
        db.rename_column(u'imagetask_imagetask', 'correctAnswer1_id', 'correctAnswer1')
        # Changing field 'ImageTask.correctAnswer1'
        db.alter_column(u'imagetask_imagetask', 'correctAnswer1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    models = {
        u'imagetask.checkboxmatrixanswer': {
            'Meta': {'object_name': 'CheckboxMatrixAnswer'},
            'answer': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cbmanswer'", 'to': u"orm['imagetask.CheckboxMatrixQuestion']"})
        },
        u'imagetask.checkboxmatrixquestion': {
            'Meta': {'object_name': 'CheckboxMatrixQuestion'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        },
        u'imagetask.formcompletiontask': {
            'Meta': {'object_name': 'FormCompletionTask'},
            'checkboxMatrixQuestions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.CheckboxMatrixQuestion']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_task_ids': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.ImageTask']", 'symmetrical': 'False'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.Question']", 'symmetrical': 'False'}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'98b6d32c95804f5ebf076d9edf2a3d52'", 'unique': 'True', 'max_length': '32'})
        },
        u'imagetask.image': {
            'Meta': {'object_name': 'Image'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'width': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'imagetask.imageanswer': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ImageAnswer'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['imagetask.Image']", 'unique': 'True'}),
            'imagetask': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'answersGiven'", 'symmetrical': 'False', 'to': u"orm['imagetask.ImageTask']"})
        },
        u'imagetask.imagetask': {
            'Meta': {'object_name': 'ImageTask'},
            'correctAnswer1': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'correctAnswer1'", 'unique': 'True', 'to': u"orm['imagetask.Image']"}),
            'correctAnswer2': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'correctAnswer2'", 'unique': 'True', 'to': u"orm['imagetask.Image']"}),
            'correctAnswer3': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'correctAnswer3'", 'unique': 'True', 'to': u"orm['imagetask.Image']"}),
            'correctImageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'images+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'c934387fbc5848c28cd2eb7f3fb1418f'", 'unique': 'True', 'max_length': '32'})
        },
        u'imagetask.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'correct_answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['imagetask']