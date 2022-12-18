from django.http import HttpResponse, HttpResponseNotFound,Http404
from django.shortcuts import render, redirect

from .forms import FormForCall
from .models import *
from django.views.generic import ListView
from .utils import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Залы", 'url_name': 'halls'},
        {'title': "Тренеры", 'url_name': 'trainers'},
        {'title': "Отзывы", 'url_name': 'reviews'},
        {'title': "Акции", 'url_name': 'sales'},
        {'title': "Абонементы", 'url_name': 'subscriptions'},
        {'title': "Личный кабинет", 'url_name': 'login'}
]


class Home(ListView):
    model = Service
    template_name = 'fitness/index.html'
    context_object_name = 'service'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['client'] = Client.objects.all()
        context['trainer'] = Employee.objects.all()
        context['discount'] = Discount.objects.all()
        context['subscription'] = Subscription.objects.all()
        context['feedback'] = Feedback.objects.all()
        #form = FormForCall()
        #context['form'] = form
        return context


class Subscriptions(ListView):
    model = Subscription
    template_name = 'fitness/subscriptions.html'
    context_object_name = 'subscription'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Абонементы'
        context['service'] = Service.objects.all()[:3]
        return context


class Trainers(ListView):
    model = Employee
    template_name = 'fitness/trainers.html'
    context_object_name = 'employee'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Тренеры'
        context['service'] = Service.objects.all()
        return context


class Halls(ListView):
    model = Service
    template_name = 'fitness/halls.html'
    context_object_name = 'service'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Залы'
        return context
#def index(request):
#    posts = Client.objects.all()
#    context = {
#        'title': 'Главная страница',
#        'menu': menu,
#        'posts': posts
#    }
#    return render(request, 'fitness/index.html', context=context)


#def halls(request):
#    return HttpResponse("<h1>Залы</h1>")


#def trainers(request):
#    return HttpResponse("<h1>Тренеры</h1>")


def reviews(request):
    return HttpResponse("<h1>Отзывы</h1>")

def sales(request):
    return HttpResponse("<h1>Скидки</h1>")


#def subscriptions(request):
#    return HttpResponse("<h1>Абонементы</h1>")


def login(request):
    return HttpResponse("<h1>Вход в лк</h1>")


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Страница приложения fitness</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2022:
        raise Http404()
    if int(year) == 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")