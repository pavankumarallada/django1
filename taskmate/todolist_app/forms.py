from django import forms
from todolist_app.models import TaskList    

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['taskname','done']   # expose only the taskname and done fields in the form
        