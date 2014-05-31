from django.shortcuts import render
from imagetask.models import Image

def student(request, template_name='imagetask/student.html'):
    images = Image.enabled_objects.all()
    data = dict(images=images)
    return render(request, template_name, data)
