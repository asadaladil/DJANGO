from django import forms
from list.models import ToDoModel
class ToDoForm(forms.ModelForm):
    class Meta:
        model=ToDoModel
        fields =['title','description']