from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'name': 'mail', 'id': 'date_of_birth', 'type':'date'}),
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


class HallsForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'filter', 'id': 'name'}),
        }

    item_id = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'id_hall', 'class': 'form-control'}))
    start = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'start', 'id': 'start',
                                                    'type': 'date'}))
    end = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'end', 'id': 'end',
                                   'type': 'date'}))

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(HallsForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['start'].required = False
        self.fields['end'].required = False
        self.fields['item_id'].required = False


class HallCreateForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name', 'description', 'max_clients', 'start_work_holidays', 'end_work_holidays','start_work_weekends', 'end_work_weekends',]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'id': 'name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'rows': '3'}),
            'max_clients': forms.NumberInput(attrs={'class': 'form-control', 'id': 'max_clients'}),
            'start_work_holidays': forms.TimeInput(attrs={'class': 'form-control',  'id': 'start_holidays',
                                                    'type': 'time'}),
            'end_work_holidays': forms.TimeInput(attrs={'class': 'form-control',  'id': 'end_holidays',
                       'type': 'time'}),
            'start_work_weekends': forms.TimeInput(attrs={'class': 'form-control', 'id': 'start_weekends',
                                                        'type': 'time'}),
            'end_work_weekends': forms.TimeInput(attrs={'class': 'form-control', 'id': 'end_weekends',
                                                        'type': 'time'}),
        }

    item_id = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'id_hall', 'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(HallCreateForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['start_work_holidays'].required = False
        self.fields['end_work_holidays'].required = False
        self.fields['start_work_weekends'].required = False
        self.fields['end_work_weekends'].required = False
        self.fields['item_id'].required = False
        self.fields['description'].required = False
        self.fields['max_clients'].required = False


#class UserCreateForm(UserCreationForm):
   # username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__phone phone', 'type': 'tel', 'placeholder':'+7(___)___-__-__', 'size':'20'}))
    #password1 = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__phone phone', 'type':'password', 'placeholder':'Пароль', 'size':'20'}))
    #password2 = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__phone phone', 'type': 'password', 'placeholder': 'Пароль', 'size': '20'}))
    #mob = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form__phone phone','placeholder': 'Телефон', 'size': '20', 'max_length':'11',}))
    #class Meta:
        #model = User
        #fields = ['username', 'password1', 'password2', 'mob']
        #widgets = {
            #'username': forms.TextInput(attrs={'class': 'form__phone phone', 'type': 'tel', 'placeholder':'+7(___)___-__-__', 'size':'20'}),
            #'password1': forms.TextInput(attrs={'class': 'form__phone phone', 'type':'password', 'placeholder':'Пароль', 'size':'20'}),
            #'password2': forms.TextInput(attrs={'class': 'form__phone phone', 'type': 'password', 'placeholder': 'Пароль', 'size': '20'}),
        #}


