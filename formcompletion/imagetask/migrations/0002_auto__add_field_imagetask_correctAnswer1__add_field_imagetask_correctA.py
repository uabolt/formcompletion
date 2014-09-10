# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ImageTask.correctAnswer1'
        db.add_column(u'imagetask_imagetask', 'correctAnswer1',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'ImageTask.correctAnswer2'
        db.add_column(u'imagetask_imagetask', 'correctAnswer2',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'ImageTask.correctAnswer3'
        db.add_column(u'imagetask_imagetask', 'correctAnswer3',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ImageTask.correctAnswer1'
        db.delete_column(u'imagetask_imagetask', 'correctAnswer1')

        # Deleting field 'ImageTask.correctAnswer2'
        db.delete_column(u'imagetask_imagetask', 'correctAnswer2')

        # Deleting field 'ImageTask.correctAnswer3'
        db.delete_column(u'imagetask_imagetask', 'correctAnswer3')


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
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'f3c9c483800548938520694c17450cab'", 'unique': 'True', 'max_length': '32'})
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
            'imagetask': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answersGiven'", 'to': u"orm['imagetask.ImageTask']"})
        },
        u'imagetask.imagetask': {
            'Meta': {'object_name': 'ImageTask'},
            'correctAnswer1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'correctAnswer2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'correctAnswer3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'correctImageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'images+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'d5f24bbc45c04cc2af048fd7bcc8b35a'", 'unique': 'True', 'max_length': '32'})
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