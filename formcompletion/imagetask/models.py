from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='images')
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
