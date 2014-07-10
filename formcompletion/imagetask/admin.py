from django.contrib import admin
from imagetask.models import Image, ImageTask, Question, FormCompletionTask, ImageAnswer

class ImageAnswerInline(admin.StackedInline):
    """
    allow the provision of answers where questions are defined

    not used
    """
    #TODO rm
    model = ImageAnswer
    extra = 3 # 3 image answer

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')
    list_filter = ('enabled',)

class ImageTaskAdmin(admin.ModelAdmin):
    #fields = ['task_code', 'images']
    inlines = [ImageAnswerInline]

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text']

admin.site.register(Image, ImageAdmin)
admin.site.register(ImageTask, ImageTaskAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FormCompletionTask)
