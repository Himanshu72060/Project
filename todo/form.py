from django import forms
from .models import FirstTodo


class TodoRegistrations(forms.ModelForm):
    class Meta:
        model = FirstTodo
        fields = ['title', 'status', 'deadline', 'description']
