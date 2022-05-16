from django import forms
from django.forms import ModelForm
from .models import TodoTask

class TodoTaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task here...', 'background-color': 'blue'}))

    class Meta:
        model = TodoTask
        fields = "__all__"