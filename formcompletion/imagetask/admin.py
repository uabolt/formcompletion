from django.contrib import admin
from imagetask import models

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')
    list_filter = ('enabled',)

admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.ImageTask)
