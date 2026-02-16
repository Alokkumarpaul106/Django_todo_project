from django import forms
from .models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model=Task
        exclude=['user'] #exclude means that je field gulo form e dekhabe na,auto save hobe
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date'}),
            'due_time':forms.TimeInput(attrs={'type':'time'}),
        }