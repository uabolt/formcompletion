from django.contrib import admin
from imagetask.models import Image, ImageTask, Question, CheckboxMatrixQuestion,\
CheckboxMatrixAnswer, FormCompletionTask, ImageAnswer #, ImageCorrectAnswer 
from forms import ImageTaskAdminForm
from re import compile, search    

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
    #form = ImageTaskAdminForm
    fields = ['task_code', 'images', 'correct_Ans_1', 'correct_Ans_2',
            'correct_Ans_3']
    # inlines = [ImageAnswerInline]

    # def save_model(self, request, obj, form, change):
    #     ordering = {}
    #     pat = compile('answersGiven-(\d+)-image$') 
    #     for key,val in request.POST.items(): #TODO use inlines from abv.
    #         result = search(pat, key)
    #         if result and val: 
    #             id = result.groups()[0]
    #             ordering[id] = int(val)
    #     ordering_list = [ordering[key] for key in sorted(ordering.keys())]
    #     #obj.set_imagecorrectanswer_order(ordering_list)
    #     obj.correctImageOrder = str(ordering_list)

    #     #print ordering_list
    #     obj.save() 


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'correct_answer']

class CBMAnswerInline(admin.StackedInline):
    model = CheckboxMatrixAnswer
    
class CheckboxMatrixQuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'size']
    inlines = [CBMAnswerInline]
    pass

class FormCompletionTaskAdmin(admin.ModelAdmin):
    view_on_site = True


admin.site.register(Image, ImageAdmin)
admin.site.register(ImageTask, ImageTaskAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(CheckboxMatrixQuestion, \
        CheckboxMatrixQuestionAdmin)
admin.site.register(FormCompletionTask, FormCompletionTaskAdmin)
