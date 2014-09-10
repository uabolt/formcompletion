# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field correctAnswer2 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correctAnswer2'))

        # Removing M2M table for field correctAnswer3 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correctAnswer3'))

        # Removing M2M table for field correctAnswer1 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correctAnswer1'))

        # Adding M2M table for field correct_Ans_1 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_correct_Ans_1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

        # Adding M2M table for field correct_Ans_2 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_correct_Ans_2')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

        # Adding M2M table for field correct_Ans_3 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_correct_Ans_3')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])


    def backwards(self, orm):
        # Adding M2M table for field correctAnswer2 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_correctAnswer2')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

        # Adding M2M table for field correctAnswer3 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_correctAnswer3')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

        # Adding M2M table for field correctAnswer1 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_correctAnswer1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

        # Removing M2M table for field correct_Ans_1 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correct_Ans_1'))

        # Removing M2M table for field correct_Ans_2 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correct_Ans_2'))

        # Removing M2M table for field correct_Ans_3 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correct_Ans_3'))


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
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'26b38499c7a24381ae3f6cfa7abef6af'", 'unique': 'True', 'max_length': '32'})
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
            'Meta': {'object_name': 'ImageAnswer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['imagetask.Image']", 'unique': 'True'})
        },
        u'imagetask.imagetask': {
            'Meta': {'object_name': 'ImageTask'},
            'correctImageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'correct_Ans_1': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage1'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'correct_Ans_2': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage2+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'correct_Ans_3': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage3+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'images+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'293929393b134986a81f23ec0b04dd0b'", 'unique': 'True', 'max_length': '32'})
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