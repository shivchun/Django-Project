from  django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=60,widget=forms.TextInput(
            attrs={'class' : 'todo_form'}))
