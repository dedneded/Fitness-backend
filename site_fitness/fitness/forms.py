from django import forms
from .models import *


class FormForCall(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form__phone phone'}),
            'phone': forms.TextInput(attrs={'class': 'form__phone phone'}),
        }


class ClientsForm(forms.ModelForm):


    class Meta:
        model = Client
        fields = ['name', 'phone', 'mail']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'name', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'name': 'phone', 'id': 'phone'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'name': 'mail', 'id': 'mail'}),

        }

    item_id = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'id_client', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ClientsForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['phone'].required = False
        self.fields['mail'].required = False
        self.fields['item_id'].required = False

class ClientCreateForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name', 'phone', 'mail', 'date_of_birth', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'name', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'name': 'phone', 'id': 'phone'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'name': 'mail', 'id': 'mail'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'name': 'mail', 'id': 'date_of_birth'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'name': 'mail', 'id': 'date_of_birth', 'rows': '6' }),

        }

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now

        self.fields['mail'].required = False
        self.fields['date_of_birth'].required = False
        self.fields['comment'].required = False


