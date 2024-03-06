from django import forms
from .models import Todo
from .views import *


class TodoForm(forms.Form):
    SUBJECT_CHOICES = (('DONE', 'done'), ('IN_PROGRESS', 'in progress'), ('DRAFT', 'draft'))
    title = forms.CharField(max_length=255, label='Title')
    description = forms.CharField(widget=forms.Textarea, required=True, label='Description')
    status = forms.ChoiceField(choices=SUBJECT_CHOICES)


class TodoFormUpdate(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TodoFormUpdate, self).__init__()
    #     # todo_all = Todo.objects.get(id=kwargs.get)
    #     self.fields['title'].queryset = Todo.objects.all()

    class Meta:
        model = Todo
        fields = ['title', 'description', 'status']
