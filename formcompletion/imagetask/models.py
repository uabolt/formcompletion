from django.db import models
import uuid

class EnabledImageManager(models.Manager):
    def get_queryset(self):
        return super(EnabledImageManager, self).get_queryset().filter(enabled=True)

class Image(models.Model):
    title = models.CharField(max_length=50)
    file = models.ImageField(upload_to='images', width_field='width', \
            height_field='height')
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    enabled = models.BooleanField(default=True)

    objects = models.Manager()
    enabled_objects = EnabledImageManager()
            

    def __unicode__(self):
        return self.title


class ImageTask(models.Model):
    task_code = models.CharField(max_length=32, unique=True, default=lambda:uuid.uuid4().hex)
    images = models.ManyToManyField(Image, related_name='images+')
    #answers = models.ManyToManyField(Image, related_name='answers+')

    def __unicode__(self):
        return self.task_code

    @models.permalink
    def student_url(self):
        return ('imagetask_student', [self.task_code])

    @models.permalink
    def teacher_url(self):
        return ('imagetask_teacher', [self.task_code])

    def get_absolute_url(self):
        return self.teacher_url()

class ImageAnswer(models.Model):
    """
    used to capture the order of image answers, via metadata option 'order_with_respect_to'
    """
    image = models.OneToOneField(Image)
    imagetask = models.ForeignKey(ImageTask, related_name='imageanswer')

    def __unicode__(self):
        return self.image.title

    class Meta:
        order_with_respect_to = 'imagetask'
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    objects = models.Manager()
    answer = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question_text
    
class FormCompletionTask(models.Model):
    task_code = models.CharField(max_length=32, unique=True, 
            default=lambda:uuid.uuid4().hex)
    questions = models.ManyToManyField(Question)
    image_task_ids = models.ManyToManyField(ImageTask) #TODO ch to imagetask (no '_'

    def __unicode__(self):
        return self.task_code

