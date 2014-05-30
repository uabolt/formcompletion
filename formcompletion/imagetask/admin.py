from django.contrib import admin
from imagetask.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')
    list_filter = ('enabled',)

admin.site.register(Image, ImageAdmin)
