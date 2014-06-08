from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('imagetask.views',
        url(r'^student/(?P<task_code>\w+)/$', 'student', name='imagetask_student'),
        url(r'^teacher/(?P<task_code>\w+)/$', 'teacher', name='imagetask_teacher'),
        url(r'^teacher/$', 'teacher_new', name='imagetask_teacher_new'),
        url(r'^answers/$', 'student_answers', name='imagetask_answers'),
        url(r'^done/$', TemplateView.as_view(template_name='imagetask/done.html'), name='imagetask_done'),
        url(r'^error/$', TemplateView.as_view(template_name='imagetask/error.html'), name='imagetask_error'),
)
