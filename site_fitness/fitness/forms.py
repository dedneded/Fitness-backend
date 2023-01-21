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
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'filter', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'name': 'filter', 'id': 'phone'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'name': 'filter', 'id': 'mail'}),

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

class EmployeesForm(forms.ModelForm):


    class Meta:
        model = Employee
        fields = ['name', 'phone', 'mail']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'filter', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'name': 'filter', 'id': 'phone'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'name': 'filter', 'id': 'mail'}),


        }

    CHOICES = [('0', 'Место работы'), ('1', 'Зал единоборств'), ('2', 'Тренажерный зал'), ('3', 'Студия баланса'), ('4', 'Зона стретчинга'),
               ('5', 'Кардиозона'), ('6', 'Водный комплекс'), ('7', 'Фитнес-кафе'), ('8', 'Массажный кабинет'),
               ('9', 'Кабинет диетолога')]
    item_id = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'id_employee', 'class': 'form-control'}))
    place_of_work = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select mt-4 '}))

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EmployeesForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['phone'].required = False
        self.fields['mail'].required = False
        self.fields['item_id'].required = False
        self.fields['place_of_work'].required = False


class EmployeeCreateForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'phone', 'mail', 'date_of_birth', 'is_hourly', 'sport_category', 'text_for_visit', 'comment']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'id': 'mail'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'name': 'date_of_birth', 'id': 'birthday',
                                                    'type': 'date'}),
            'comment': forms.Textarea(attrs={'class': 'form-control',  'id': 'comment',  'rows': '3'}),
            'text_for_visit': forms.Textarea(attrs={'class': 'form-control', 'id': 'text_for_visit', 'rows': '1'}),
            'sport_category':  forms.Select(attrs={'class': 'form-select'}),
            'is_hourly': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'name':'flexRadioDefault', 'id': 'is_hourly'})




        }

    CHOICES = [('0', 'Место работы'), ('1', 'Зал единоборств'), ('2', 'Тренажерный зал'), ('3', 'Студия баланса'), ('4', 'Зона стретчинга'),
               ('5', 'Кардиозона'), ('6', 'Водный комплекс'), ('7', 'Фитнес-кафе'), ('8', 'Массажный кабинет'),
               ('9', 'Кабинет диетолога')]

    place_of_work = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['phone'].required = False
        self.fields['mail'].required = False
        self.fields['place_of_work'].required = False
        self.fields['date_of_birth'].required = False
        self.fields['comment'].required = False
        self.fields['text_for_visit'].required = False
        self.fields['sport_category'].required = False


