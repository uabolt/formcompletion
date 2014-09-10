# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ImageTask.correctAnswer2'
        db.delete_column(u'imagetask_imagetask', 'correctAnswer2_id')

        # Deleting field 'ImageTask.correctAnswer3'
        db.delete_column(u'imagetask_imagetask', 'correctAnswer3_id')

        # Deleting field 'ImageTask.correctAnswer1'
        db.delete_column(u'imagetask_imagetask', 'correctAnswer1_id')

        # Adding M2M table for field correctAnswer1 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_correctAnswer1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

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


    def backwards(self, orm):
        # Adding field 'ImageTask.correctAnswer2'
        db.add_column(u'imagetask_imagetask', 'correctAnswer2',
                      self.gf('django.db.models.fields.related.OneToOneField')(default='', related_name='correctAnswer2', unique=True, to=orm['imagetask.Image']),
                      keep_default=False)

        # Adding field 'ImageTask.correctAnswer3'
        db.add_column(u'imagetask_imagetask', 'correctAnswer3',
                      self.gf('django.db.models.fields.related.OneToOneField')(default='', related_name='correctAnswer3', unique=True, to=orm['imagetask.Image']),
                      keep_default=False)

        # Adding field 'ImageTask.correctAnswer1'
        db.add_column(u'imagetask_imagetask', 'correctAnswer1',
                      self.gf('django.db.models.fields.related.OneToOneField')(default='', related_name='correctAnswer1', unique=True, to=orm['imagetask.ImageAnswer']),
                      keep_default=False)

        # Removing M2M table for field correctAnswer1 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correctAnswer1'))

        # Removing M2M table for field correctAnswer2 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correctAnswer2'))

        # Removing M2M table for field correctAnswer3 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correctAnswer3'))


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
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'ae4fbeac53b04f63a662f0ca0470a5f1'", 'unique': 'True', 'max_length': '32'})
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
            'correctAnswer1': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage1+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'correctAnswer2': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage2+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'correctAnswer3': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage3+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'correctImageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'images+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'561c74a4d12e422db7dd6be1014f55b3'", 'unique': 'True', 'max_length': '32'})
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