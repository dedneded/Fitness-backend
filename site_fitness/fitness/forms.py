from django import forms
from .models import *


class FormForCall(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form__phone phone'}),
            'phone': forms.TextInput(attrs={'class': 'form__phone phone'})
        }