from django.conf.urls import patterns, url

urlpatterns = patterns('imagetask.views',
        url(r'^student/$', 'student', name='imagetask_student'),
)