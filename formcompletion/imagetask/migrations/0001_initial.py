# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'imagetask_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'imagetask', ['Image'])

        # Adding model 'ImageAnswer'
        db.create_table(u'imagetask_imageanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imagetask.Image'], unique=True)),
        ))
        db.send_create_signal(u'imagetask', ['ImageAnswer'])

        # Adding model 'ImageTask'
        db.create_table(u'imagetask_imagetask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_code', self.gf('django.db.models.fields.CharField')(default='fb2a7429d25a4e8ba3ef3734dde2c8d7', unique=True, max_length=32)),
            ('correctImageOrder', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imageOrder', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'imagetask', ['ImageTask'])

        # Adding M2M table for field images on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

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

        # Adding M2M table for field given_Ans_1 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_given_Ans_1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

        # Adding M2M table for field given_Ans_2 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_given_Ans_2')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

        # Adding M2M table for field given_Ans_3 on 'ImageTask'
        m2m_table_name = db.shorten_name(u'imagetask_imagetask_given_Ans_3')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False)),
            ('image', models.ForeignKey(orm[u'imagetask.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagetask_id', 'image_id'])

        # Adding model 'Question'
        db.create_table(u'imagetask_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correct_answer', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'imagetask', ['Question'])

        # Adding model 'TextAnswer'
        db.create_table(u'imagetask_textanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'imagetask', ['TextAnswer'])

        # Adding model 'CheckboxMatrixQuestion'
        db.create_table(u'imagetask_checkboxmatrixquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'imagetask', ['CheckboxMatrixQuestion'])

        # Adding model 'CheckboxMatrixAnswer'
        db.create_table(u'imagetask_checkboxmatrixanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cbmanswer', to=orm['imagetask.CheckboxMatrixQuestion'])),
            ('answer', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'imagetask', ['CheckboxMatrixAnswer'])

        # Adding model 'FormCompletionTaskAnswers'
        db.create_table(u'imagetask_formcompletiontaskanswers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('textAnswers', self.gf('django.db.models.fields.related.ForeignKey')(related_name='textAnswers', to=orm['imagetask.TextAnswer'])),
            ('cbmAnswers', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cbmAnswers', to=orm['imagetask.CheckboxMatrixAnswer'])),
            ('imageAnswers', self.gf('django.db.models.fields.related.ForeignKey')(related_name='imageAnswers', to=orm['imagetask.ImageAnswer'])),
        ))
        db.send_create_signal(u'imagetask', ['FormCompletionTaskAnswers'])

        # Adding model 'FormCompletionTask'
        db.create_table(u'imagetask_formcompletiontask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_code', self.gf('django.db.models.fields.CharField')(default='110cdbc423fd4e3894ee39b82d40b7bd', unique=True, max_length=32)),
            ('formCompletionAnswers', self.gf('django.db.models.fields.related.OneToOneField')(related_name='formcompletionAnswers', unique=True, to=orm['imagetask.FormCompletionTaskAnswers'])),
            ('bar', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal(u'imagetask', ['FormCompletionTask'])

        # Adding M2M table for field questions on 'FormCompletionTask'
        m2m_table_name = db.shorten_name(u'imagetask_formcompletiontask_questions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formcompletiontask', models.ForeignKey(orm[u'imagetask.formcompletiontask'], null=False)),
            ('question', models.ForeignKey(orm[u'imagetask.question'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formcompletiontask_id', 'question_id'])

        # Adding M2M table for field checkboxMatrixQuestions on 'FormCompletionTask'
        m2m_table_name = db.shorten_name(u'imagetask_formcompletiontask_checkboxMatrixQuestions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formcompletiontask', models.ForeignKey(orm[u'imagetask.formcompletiontask'], null=False)),
            ('checkboxmatrixquestion', models.ForeignKey(orm[u'imagetask.checkboxmatrixquestion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formcompletiontask_id', 'checkboxmatrixquestion_id'])

        # Adding M2M table for field image_task_ids on 'FormCompletionTask'
        m2m_table_name = db.shorten_name(u'imagetask_formcompletiontask_image_task_ids')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formcompletiontask', models.ForeignKey(orm[u'imagetask.formcompletiontask'], null=False)),
            ('imagetask', models.ForeignKey(orm[u'imagetask.imagetask'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formcompletiontask_id', 'imagetask_id'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'imagetask_image')

        # Deleting model 'ImageAnswer'
        db.delete_table(u'imagetask_imageanswer')

        # Deleting model 'ImageTask'
        db.delete_table(u'imagetask_imagetask')

        # Removing M2M table for field images on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_images'))

        # Removing M2M table for field correct_Ans_1 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correct_Ans_1'))

        # Removing M2M table for field correct_Ans_2 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correct_Ans_2'))

        # Removing M2M table for field correct_Ans_3 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_correct_Ans_3'))

        # Removing M2M table for field given_Ans_1 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_given_Ans_1'))

        # Removing M2M table for field given_Ans_2 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_given_Ans_2'))

        # Removing M2M table for field given_Ans_3 on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_given_Ans_3'))

        # Deleting model 'Question'
        db.delete_table(u'imagetask_question')

        # Deleting model 'TextAnswer'
        db.delete_table(u'imagetask_textanswer')

        # Deleting model 'CheckboxMatrixQuestion'
        db.delete_table(u'imagetask_checkboxmatrixquestion')

        # Deleting model 'CheckboxMatrixAnswer'
        db.delete_table(u'imagetask_checkboxmatrixanswer')

        # Deleting model 'FormCompletionTaskAnswers'
        db.delete_table(u'imagetask_formcompletiontaskanswers')

        # Deleting model 'FormCompletionTask'
        db.delete_table(u'imagetask_formcompletiontask')

        # Removing M2M table for field questions on 'FormCompletionTask'
        db.delete_table(db.shorten_name(u'imagetask_formcompletiontask_questions'))

        # Removing M2M table for field checkboxMatrixQuestions on 'FormCompletionTask'
        db.delete_table(db.shorten_name(u'imagetask_formcompletiontask_checkboxMatrixQuestions'))

        # Removing M2M table for field image_task_ids on 'FormCompletionTask'
        db.delete_table(db.shorten_name(u'imagetask_formcompletiontask_image_task_ids'))


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
            'bar': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'checkboxMatrixQuestions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.CheckboxMatrixQuestion']", 'symmetrical': 'False'}),
            'formCompletionAnswers': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'formcompletionAnswers'", 'unique': 'True', 'to': u"orm['imagetask.FormCompletionTaskAnswers']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_task_ids': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.ImageTask']", 'symmetrical': 'False'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.Question']", 'symmetrical': 'False'}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'b0a99180c5e14bb0913b52814f3843c0'", 'unique': 'True', 'max_length': '32'})
        },
        u'imagetask.formcompletiontaskanswers': {
            'Meta': {'object_name': 'FormCompletionTaskAnswers'},
            'cbmAnswers': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cbmAnswers'", 'to': u"orm['imagetask.CheckboxMatrixAnswer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageAnswers': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imageAnswers'", 'to': u"orm['imagetask.ImageAnswer']"}),
            'textAnswers': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'textAnswers'", 'to': u"orm['imagetask.TextAnswer']"})
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
            'correct_Ans_1': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage1+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'correct_Ans_2': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage2+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'correct_Ans_3': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'correctImage3+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'given_Ans_1': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'givenImage1+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'given_Ans_2': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'givenImage2+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'given_Ans_3': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'givenImage3+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'images+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'e429d34f47db4f96b5715342d68514d8'", 'unique': 'True', 'max_length': '32'})
        },
        u'imagetask.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'correct_answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'imagetask.textanswer': {
            'Meta': {'object_name': 'TextAnswer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['imagetask']