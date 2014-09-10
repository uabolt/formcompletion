# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ImageAnswer.imagetask'
        db.delete_column(u'imagetask_imageanswer', 'imagetask_id')

        # Adding M2M table for field imagetask on 'ImageAnswer'
        m2m_table_name = db.shorten_name(u'imagetask_imageanswer_imagetask')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imageanswer', models.ForeignKey(orm[u'imagetask.imageanswer'], null=False)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imageanswer_id', 'imagetask_id'])


    def backwards(self, orm):
        # Adding field 'ImageAnswer.imagetask'
        db.add_column(u'imagetask_imageanswer', 'imagetask',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='answersGiven', to=orm['imagetask.ImageTask']),
                      keep_default=False)

        # Removing M2M table for field imagetask on 'ImageAnswer'
        db.delete_table(db.shorten_name(u'imagetask_imageanswer_imagetask'))


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
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'2282106003f64069b351853419c208fc'", 'unique': 'True', 'max_length': '32'})
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
            'correctAnswer1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'correctAnswer2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'correctAnswer3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'correctImageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'images+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'95298dfbf3654ada8f9cd29d654feb6c'", 'unique': 'True', 'max_length': '32'})
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