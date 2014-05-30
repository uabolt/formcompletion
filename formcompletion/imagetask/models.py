from django.db import models

class EnabledImageManager(models.Manager):
    def get_queryset(self):
        return super(EnabledImageManager, self).get_queryset().filter(enabled=True)

class Image(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='images')
    enabled = models.BooleanField(default=True)

    objects = models.Manager()
    enabled_objects = EnabledImageManager()

    def __unicode__(self):
        return self.title
