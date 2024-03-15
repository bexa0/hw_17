from django import forms
from django.forms import ModelForm
from app17.models import Task


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline', 'image']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'})
        }
        required = ['title', 'description', 'priority', 'deadline', 'image']


class Settings(forms.Form):
    choises_for_order = [('title', 'В алфавитном порядке названия'), ('deadline', 'По близости дедлайна'), ('priority', 'По приоритетам')]
    choises_for_theme = [('black', 'Темный'), ('white', 'Светлый')]

    theme = forms.ChoiceField(widget=forms.RadioSelect, choices=choises_for_theme)
    order = forms.ChoiceField(widget=forms.RadioSelect, choices=choises_for_order)
    clear_task_history = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    clear_action_history = forms.BooleanField(widget=forms.CheckboxInput() ,required=False)
