from django import forms

class TodoForm(forms.Form):
    form_text = forms.CharField(max_length=30 ,widget= forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'A Django Todo'
    }))
