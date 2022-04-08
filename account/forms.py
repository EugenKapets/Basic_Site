from django import forms
from django.forms import ModelForm , TextInput, Textarea
from .models import Task

class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ["title","task"]
        widgets = {"title": TextInput(attrs= {
            'class' : 'entername', 
            'placeholder' : 'Enter the name blog'}),
            "task": Textarea(attrs= {
            'class' : 'Content Blog', 
            'placeholder' : 'Content Blog'}),
        }