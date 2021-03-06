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


class ImageAnswer(models.Model):
    """
    used to capture the order of image answers, via metadata option 'order_with_respect_to'
    """
    image = models.OneToOneField(Image)
    #imagetask = models.ManyToManyField(ImageTask, related_name='answersGiven')

    def __unicode__(self):
        return self.image.title

    #class Meta:
    #    order_with_respect_to = 'imagetask'

class ImageTask(models.Model):
    task_code = models.CharField(max_length=32, unique=True, default=lambda:uuid.uuid4().hex)
    images = models.ManyToManyField(Image, related_name='images+')
    correctImageOrder = models.CharField(max_length=200) # TODO rm. string, for now

    correct_Ans_1 = models.ManyToManyField(Image,
            related_name='correctImage1+')
    correct_Ans_2 = models.ManyToManyField(Image, related_name='correctImage2+')
    correct_Ans_3 = models.ManyToManyField(Image, related_name='correctImage3+')

    given_Ans_1 = models.ManyToManyField(Image, related_name='givenImage1+')
    given_Ans_2 = models.ManyToManyField(Image, related_name='givenImage2+')
    given_Ans_3 = models.ManyToManyField(Image, related_name='givenImage3+')

    imageOrder = models.CharField(max_length=200) # TODO string, for now

    def __unicode__(self):
        return self.task_code 


""" TODO
class ImageCorrectAnswer(models.Model):
    image = models.ManyToManyField(Image)
    imagetask = models.ForeignKey(ImageTask, related_name='correctAnswers')

    class Meta:
        order_with_respect_to = 'imagetask'
"""

class Question(models.Model): # TODO rename to TextQuestion
    question_text = models.CharField(max_length=200, blank=True)
    objects = models.Manager()
    answer = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200) #TODO make a class like CheckboxMatrixAnswer etc

    def __unicode__(self):
        return self.question_text

class TextAnswer(models.Model):
    answer = models.CharField(max_length=200, blank=True)

class CheckboxMatrixQuestion(models.Model):
    question_text = models.CharField(max_length=200, blank=True)
    size = models.IntegerField() # the size of the square matrix of checkboxes #TODO change to sidelength?
    answer = models.CharField(max_length=500) # users input, as a comma-sep str of "false" and "true"

class CheckboxMatrixAnswer(models.Model):
    question = models.ForeignKey(CheckboxMatrixQuestion, related_name='cbmanswer')
    answer = models.BooleanField()
    
class FormCompletionTaskAnswers(models.Model):
    textAnswers = models.ForeignKey(TextAnswer, related_name='textAnswers')
    cbmAnswers = models.ForeignKey(CheckboxMatrixAnswer,
            related_name='cbmAnswers')
    imageAnswers = models.ForeignKey(ImageAnswer, related_name='imageAnswers')

class FormCompletionTask(models.Model):
    task_code = models.CharField(max_length=32, unique=True, 
            default=lambda:uuid.uuid4().hex)
    questions = models.ManyToManyField(Question) # TODO rename to 'textQuestions'
    checkboxMatrixQuestions = \
            models.ManyToManyField(CheckboxMatrixQuestion)
    image_task_ids = models.ManyToManyField(ImageTask) #TODO ch to imagetask (no '_')
    formCompletionAnswers = models.OneToOneField(FormCompletionTaskAnswers,
            related_name='formcompletionAnswers', blank=True, null=True)


    @models.permalink
    def student_url(self):
        return ('imagetask_student', [self.task_code])

    @models.permalink
    def teacher_url(self):
        return ('imagetask_teacher', [self.task_code])

    def __unicode__(self):
        return self.task_code

