from django.contrib import admin
from imagetask.models import Image, ImageTask, Question, CheckboxMatrixQuestion, CheckboxMatrixAnswer, \
    FormCompletionTask, ImageAnswer 

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
    fields = ['task_code', 'images']
    inlines = [ImageAnswerInline]

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'correct_answer']

class CBMAnswerInline(admin.StackedInline):
    model = CheckboxMatrixAnswer
    
class CheckboxMatrixQuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'size']
    inlines = [CBMAnswerInline]
    pass
    

admin.site.register(Image, ImageAdmin)
admin.site.register(ImageTask, ImageTaskAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(CheckboxMatrixQuestion, \
        CheckboxMatrixQuestionAdmin)
admin.site.register(FormCompletionTask)
