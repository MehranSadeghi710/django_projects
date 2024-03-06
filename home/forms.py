from django import forms
from .models import Todo
from .views import *


class TodoForm(forms.Form):
    SUBJECT_CHOICES = (('DONE', 'done'), ('IN_PROGRESS', 'in progress'), ('DRAFT', 'draft'))
    title = forms.CharField(max_length=255, label='Title')
    description = forms.CharField(widget=forms.Textarea, required=True, label='Description')
    status = forms.ChoiceField(choices=SUBJECT_CHOICES)


class TodoFormUpdate(forms.ModelForm):
    # def __init__(self):
    #     super(TodoFormUpdate, self).__init__()
    #     self.fields['title'] = TodoForm.title
    #     self.fields['description'] = TodoForm.description
    #     self.fields['status'] = TodoForm.status

    class Meta:
        model = Todo
        fields = ['title', 'description', 'status']
