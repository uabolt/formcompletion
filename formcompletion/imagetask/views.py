from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from imagetask.models import Image, ImageTask

def student(request, task_code, template_name='imagetask/student.html'):
    task = get_object_or_404(ImageTask, task_code=task_code)
    request.session['task_code'] = task_code
    images = Image.enabled_objects.all()
    data = dict(task=task, images=images)
    return render(request, template_name, data)

def teacher(request, task_code, template_name='imagetask/teacher.html'):
    task = get_object_or_404(ImageTask, task_code=task_code)
    student_url = request.build_absolute_uri(task.student_url())
    teacher_url = request.build_absolute_uri(task.teacher_url())
    data = dict(images=task.images, student_url=student_url, teacher_url=teacher_url)
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
    task = ImageTask.objects.get(task_code=task_code)

    if request.method == 'POST':
        try:
            slot1 = Image.objects.get(pk=request.POST['slot1'])
            slot2 = Image.objects.get(pk=request.POST['slot2'])
            slot3 = Image.objects.get(pk=request.POST['slot3'])
        except Image.NotFound:
            messages.error('invalid image id')
            return redirect(task.student_url())

        task.answer = [slot1, slot2, slot3]
        task.save()
        return redirect('imagetask_done')

    else:
        return redirect('imagetask_error')
