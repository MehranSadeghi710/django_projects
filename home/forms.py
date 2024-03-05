from django import forms


class TodoForm(forms.Form):
    SUBJECT_CHOICES = (('DONE', 'done'), ('IN_PROGRESS', 'in progress'), ('DRAFT', 'draft'))
    title = forms.CharField(max_length=255, label='Title')
    description = forms.CharField(widget=forms.Textarea, required=True, label='Description')
    status = forms.ChoiceField(choices=SUBJECT_CHOICES)
