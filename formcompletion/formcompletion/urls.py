from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from iraqiSpeakerVerifiers.views import SpeakerVerificationCreate, SpeakerVerificationUpdate
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^imagetask/', include('imagetask.urls')),
    url(r'iraqiSpeakerVerifier/add/$', SpeakerVerificationCreate.as_view(),
        name='verification'),
    url(r'iraqiSpeakerVerifier/(?P<pk>\d+)/$',
        SpeakerVerificationUpdate.as_view(), name='verification'),
    url(r'^done/$', TemplateView.as_view(template_name='imagetask/done.html'),
        name='answer1_done'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
