from django import forms
from django_summernote.widgets import SummernoteWidget

from . import models

class FanficForm(forms.ModelForm):
    class Meta:
        exclude = ('public', 'author', 'date', 'fandom')
        model = models.Fanfic
        widgets = {
            'text': SummernoteWidget(),
        }