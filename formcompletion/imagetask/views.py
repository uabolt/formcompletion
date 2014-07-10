from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from imagetask.models import Image, ImageTask, Question, CheckboxMatrixQuestion, FormCompletionTask
from math import sqrt

def student(request, task_code, template_name='imagetask/student.html'):
    #task = get_object_or_404(ImageTask, task_code=task_code)
    task = get_object_or_404(FormCompletionTask, task_code=task_code)
    request.session['task_code'] = task_code
    #TODO get from the task
    images = Image.enabled_objects.all()
    questions = Question.objects.all()
    #checkboxMatrixQuestions = CheckboxMatrixQuestion.objects.all()
    checkboxMatrixQuestions = task.checkboxMatrixQuestions.all()

    #TODO fix cbox matrix sizing
    boxesCount = []
    for cbmq in checkboxMatrixQuestions:
        boxesCount = range(cbmq.size)

    #TODO pass in object
    cbSqrt = int(sqrt(cbmq.size))
    data = dict(task = task, images = images, questions = questions, \
            checkboxMatrixQuestions = checkboxMatrixQuestions, \
            boxesCount = boxesCount, cbSqrt = cbSqrt)
    return render(request, template_name, data)

def teacher(request, task_code, template_name='imagetask/teacher.html'):
    task = get_object_or_404(FormCompletionTask, task_code=task_code)
    imagetask = task.image_task_ids.last() #TODO last only

    questions = task.questions.all()
    checkboxMatrixQuestions = task.checkboxMatrixQuestions.all()

    #student_url = request.build_absolute_uri(imagetask.student_url())
    #teacher_url = request.build_absolute_uri(imagetask.teacher_url())
    data = dict(images=imagetask.correctanswers, #student_url=student_url, teacher_url=teacher_url,
            questions = questions, checkboxMatrixQuestions = checkboxMatrixQuestions)
    return render(request, template_name, data)

def teacher_new(request):
    task = ImageTask()
    task.save()  # save to db before assigning many-to-many relation
    task.images = Image.enabled_objects.order_by('?')[:3]
    task.save()  # save again
    return redirect(task.teacher_url())

def student_answers(request):
    if not request.is_ajax():
        return redirect('imagetask_error')

    task_code = request.session['task_code']
    task = FormCompletionTask.objects.get(task_code=task_code)

    if request.method == 'POST':
        try:
            results = request.POST.items()
        except Image.NotFound:
            messages.error('invalid image id')
            return redirect(task.student_url())

        cbmtask = task.checkboxMatrixQuestions.last() #takes last ONLY TODO
        imagetask = task.image_task_ids.first()
        answers = []
        cbmanswers = []
        for key,val in results: # these are reversed
            if key.startswith("image_slot_"):
                answers.append(val)
            elif key.startswith("cbm"):
                cbmtask.answer = val # a string, for now TODO
                cbmtask.save()
            else:
                question = task.questions.get(id=key)
                question.answer = val
                question.save()


        imagetask.set_imageanswer_order(list(reversed(answers)))
        imagetask.save()
        task.save() #TODO needed?
        return redirect('imagetask_done')

    else:
        return redirect('imagetask_error')
