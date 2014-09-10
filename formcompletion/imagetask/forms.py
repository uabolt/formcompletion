from django import forms
from django.contrib import admin
from imagetask.models import ImageTask

class ImageTaskAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ImageTaskAdminForm, self).__init__(*args, **kwargs)
        self.fields['correctAnswer1'].widget = forms.Select()
