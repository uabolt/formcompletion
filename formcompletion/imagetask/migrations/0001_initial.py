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

        # Adding model 'ImageTask'
        db.create_table(u'imagetask_imagetask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_code', self.gf('django.db.models.fields.CharField')(default='cb0c5b233f6d42f5a2e2ca796c5e5f85', unique=True, max_length=32)),
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

        # Adding model 'ImageAnswer'
        db.create_table(u'imagetask_imageanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imagetask.Image'], unique=True)),
            ('imagetask', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answersGiven', to=orm['imagetask.ImageTask'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'imagetask', ['ImageAnswer'])

        # Adding model 'Question'
        db.create_table(u'imagetask_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correct_answer', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'imagetask', ['Question'])

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

        # Adding model 'FormCompletionTask'
        db.create_table(u'imagetask_formcompletiontask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_code', self.gf('django.db.models.fields.CharField')(default='cfe246c5da56432c91050cee9a90bead', unique=True, max_length=32)),
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

        # Deleting model 'ImageTask'
        db.delete_table(u'imagetask_imagetask')

        # Removing M2M table for field images on 'ImageTask'
        db.delete_table(db.shorten_name(u'imagetask_imagetask_images'))

        # Deleting model 'ImageAnswer'
        db.delete_table(u'imagetask_imageanswer')

        # Deleting model 'Question'
        db.delete_table(u'imagetask_question')

        # Deleting model 'CheckboxMatrixQuestion'
        db.delete_table(u'imagetask_checkboxmatrixquestion')

        # Deleting model 'CheckboxMatrixAnswer'
        db.delete_table(u'imagetask_checkboxmatrixanswer')

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
            'checkboxMatrixQuestions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.CheckboxMatrixQuestion']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_task_ids': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.ImageTask']", 'symmetrical': 'False'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagetask.Question']", 'symmetrical': 'False'}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'8838d235b5274d0a826f101348eb2783'", 'unique': 'True', 'max_length': '32'})
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
            'correctImageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageOrder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'images+'", 'symmetrical': 'False', 'to': u"orm['imagetask.Image']"}),
            'task_code': ('django.db.models.fields.CharField', [], {'default': "'c8429815a65d4226acdd9714015d228f'", 'unique': 'True', 'max_length': '32'})
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