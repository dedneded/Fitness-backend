from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from .forms import *
from .models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .utils import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Залы", 'url_name': 'halls'},
        {'title': "Тренеры", 'url_name': 'trainers'},
        #{'title': "Отзывы", 'url_name': 'reviews'},
        #{'title': "Акции", 'url_name': 'sales'},
        #{'title': "Абонементы", 'url_name': 'subscriptions'},
        #{'title': "Личный кабинет", 'url_name': 'login'}
]
menu_admin = [
        {'title': "Посещения", 'content':[{'subtitle': "Посещения по абонементу", 'url_name': 'admin_visit_by_subscription'}, {'subtitle': "Посещения услуг", 'url_name': 'admin_visits'}]},
        {'title': "Каталог", 'content':[{'subtitle': "Залы", 'url_name': 'admin_halls'}, {'subtitle': "Спорт-направления", 'url_name': 'admin_sport-services'}, {'subtitle': "Услуги", 'url_name': 'admin_services'}]},
        {'title': "Абонементы", 'content':[], 'url_name': 'admin_subscriptions'},
        {'title': "Клиенты", 'content':[], 'url_name': 'admin_clients'},
        {'title': "Сотрудники", 'content':[{'subtitle': "Все сотрудники", 'url_name': 'admin_employees'}, {'subtitle': "Расписание", 'url_name': 'admin_employee_timetable'}, {'subtitle': "Должности", 'url_name': 'admin_roles'}]},
        {'title': "Акции", 'content':[], 'url_name': 'admin_sales'},
        {'title': "Отзывы", 'content':[], 'url_name': 'admin_reviews'},
        {'title': "Дополнительно", 'content':[{'subtitle': "Настройка главной", 'url_name': 'admin_manage_main'}, {'subtitle': "Профиль", 'url_name': 'admin_profile'}]},
]

menu_client_profile = [
        {'title': "Профиль", 'url_name': 'client_services'},
        {'title': "Расписание", 'url_name': 'client_timetable'},
        {'title': "Избранное", 'url_name': 'client_favourites'},
        {'title': "История", 'url_name': 'client_history_subscriptions'},
        {'title': "Корзина", 'url_name': 'client_cart'}
]
class Home(ListView):
    model = Service
    template_name = 'fitness/index.html'
    context_object_name = 'service'
    queryset = Service.objects.filter(parent=None)

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


class ClientServices(ListView):
    model = Subscription
    template_name = 'fitness/client_profile/profile.html'
    context_object_name = 'services'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_client_profile
        context['title'] = 'Доступные услуги'

        return context

class ClientLogin(ListView):
    model = Client
    template_name = 'fitness/client_profile/login.html'
    context_object_name = 'clients'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_client_profile
        context['title'] = 'Вход в личный кабинет'

        return context


class ClientCart(ListView):
    model = Client
    template_name = 'fitness/client_profile/cart.html'
    context_object_name = 'clients'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_client_profile
        context['title'] = 'Корзина'

        return context

class ClientFavourites(ListView):
    model = Client
    template_name = 'fitness/client_profile/favourites.html'
    context_object_name = 'clients'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_client_profile
        context['title'] = 'Избранное'

        return context


class ClientHistorySubscriptions(ListView):
    model = Client
    template_name = 'fitness/client_profile/history_subscriptions.html'
    context_object_name = 'clients'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_client_profile
        context['title'] = 'История абонементов'

        return context


class ClientHistoryVisits(ListView):
    model = Client
    template_name = 'fitness/client_profile/history_visits.html'
    context_object_name = 'clients'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_client_profile
        context['title'] = 'История визитов'

        return context

class ClientPersonalData(ListView):
    model = Client
    template_name = 'fitness/client_profile/personal_data.html'
    context_object_name = 'clients'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_client_profile
        context['title'] = 'Личная информация'

        return context


class ClientTimetable(ListView):
    model = Client
    template_name = 'fitness/client_profile/timetable.html'
    context_object_name = 'clients'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_client_profile
        context['title'] = 'Расписание'
        return context


class RegisterUser(CreateView):
    #form_class = UserCreateForm
    template_name = 'fitness/client_profile/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистрация'
        return context


class AdminClients(ListView):
    paginate_by = 2
    model = Client
    template_name = 'fitness/admin/clients.html'
    context_object_name = 'client'
    filter = ""
    sort = ""

    def get(self, *args, **kwargs):
        resp = super().get(*args, **kwargs)
        return resp

    #def post(self, request, *args, **kwargs):
        #form = self.form(request.POST)
        #if form.is_valid():
            #self.filter = form.cleaned_data
           # print(self.filter)
            ## <process form cleaned data>
            #return HttpResponseRedirect('/admin_clients')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Клиенты'
        context['sort'] = self.sort
        form = ClientsForm(self.request.GET)
        context['form'] = form
        if form.is_valid() and self.request.method == "GET":
            if form.cleaned_data.get("name") or form.cleaned_data.get("phone") or form.cleaned_data.get("mail") or form.cleaned_data.get("item_id"):
                context['client'] = \
                    Client.objects.filter(name=form.cleaned_data.get("name")) \
                    | Client.objects.filter(phone=form.cleaned_data.get("phone")) | \
                    Client.objects.filter(mail=form.cleaned_data.get("mail"))\
                    | Client.objects.filter(pk=form.cleaned_data.get("item_id"))
        return context

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'give-default-value')
        order_by = self.request.GET.get('order_by', 'id')
        self.sort = order_by
        order = self.request.GET.get('orderby', 'give-default-value')
        return Client.objects.all().order_by(order_by)

        #filter_by = self.request.GET.get('filter_by', '')
        #return Client.objects.all().order_by(order_by)
    #def get_ordering(self):
        #ordering = self.request.GET.get('ordering', 'id')
       # # validate ordering here
       # return ordering


class AdminVisitBySubscription(ListView):
    pass


class AdminVisits(ListView):
    pass




class AdminSportServices(ListView):
    pass


class AdminServices(ListView):
    pass


class AdminSubscriptions(ListView):
    pass




class AdminTimetable(ListView):
    pass


class AdminRoles(ListView):
    pass


class AdminSales(ListView):
    pass


class AdminReviews(ListView):
    pass


class AdminManageMain(ListView):
    pass

class AdminProfile(ListView):
    pass


class AdminClientCreate(CreateView):
    form_class = ClientCreateForm
    template_name = 'fitness/admin/client_create.html'
    #success_url = 'fitness/admin/clients'
    context_object_name = 'client'
    model = Client

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Добавление клиента'
        context['form'] = self.form_class
        context['bredcrumbs'] = 'Добавление клиента'
        return context

    #def form_valid(self, form):
        #form_class = ClientCreateForm(self.request.POST)
        #if form_class.is_valid():
            #form_class.save()
        #Client.objects.create(**form.cleaned_data)
        #return redirect('admin_clients')

    success_message = 'Doc successfully created!'
    error_message = 'Введите поля формы корректно!'

    def get_success_url(self):
        return reverse('admin_clients')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        self.form_class = form
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class AdminClientSee(DetailView):
    model = Client
    template_name = 'fitness/admin/client_see.html'
    context_object_name = 'client'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Просмотр информации о клиенте'
        return context


class AdminClientUpdate(UpdateView):
    model = Client
    template_name = 'fitness/admin/client_update.html'
    form_class = ClientCreateForm
    context_object_name = 'client'
    #pk_url_kwarg = "client_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Редактирование клиента'
        context['bredcrumbs'] = 'Редактирование клиента'
        return context

    def get_success_url(self):
        return reverse('client_detail', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        self.form_class = form
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return super().form_invalid(form)

class AdminClientDelete(DeleteView):
    model = Client
    template_name = 'fitness/admin/client_update.html'
    success_url = reverse_lazy('admin_clients')


class AdminEmployees(ListView):
    paginate_by = 3
    model = Employee
    template_name = 'fitness/admin/employees.html'
    context_object_name = 'employee'
    filter = ""
    sort = ""

    def get(self, *args, **kwargs):
        resp = super().get(*args, **kwargs)
        return resp

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Сотрудники'
        context['sort'] = self.sort
        form = EmployeesForm(self.request.GET)
        context['form'] = form

        return context


class AdminEmployeeSee(DetailView):
    model = Employee
    template_name = 'fitness/admin/employee_see.html'
    context_object_name = 'employee'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Просмотр информации о сотруднике'
        return context


class AdminEmployeeCreate(CreateView):
    form_class = EmployeeCreateForm
    template_name = 'fitness/admin/employee_create.html'
    # success_url = 'fitness/admin/clients'
    context_object_name = 'employee'
    model = Employee

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Добавление сотрудника'
        context['form'] = self.form_class
        context['bredcrumbs'] = 'Добавление сотрудника'
        context['roles'] = Role.objects.all()
        return context


    success_message = 'Doc successfully created!'
    error_message = 'Введите поля формы корректно!'

    def get_success_url(self):
        return reverse('admin_employees')

    def form_valid(self, form):

        role_id = form.cleaned_data['id']
        role = get_object_or_404(Role, pk=role_id)
        employee = form.instance
        employee.roles.add(role)
        employee.save()
        #form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        self.form_class = form
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class AdminEmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'fitness/admin/employee_update.html'
    form_class = EmployeeCreateForm
    context_object_name = 'employee'
    roles = []

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Редактирование сотрудника'
        context['bredcrumbs'] = 'Редактирование сотрудника'
        employee = Employee.objects.get(pk=self.kwargs.get('pk'))
        self.roles = []
        for role in employee.roles.all():
            self.roles.append(role.id)
        context['roles'] = Role.objects.exclude(pk__in=self.roles)
        return context

    def get_success_url(self):
        return reverse('employee_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        pass
        #roles = form.cleaned_data['roles']
        #employee = form.instance
        #for role in roles:
            #role = get_object_or_404(Role, pk=role)
            #employee.roles.add(role)
        #employee.save()
        #form.instance.created_by = self.request.user
        #return super().form_valid(form)


    def form_invalid(self, form):
        self.form_class = form
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return super().form_invalid(form)


def add_role_view(request, pk):
    if request.method == 'POST':
        roles = request.POST.getlist('roles[]')
        employee = Employee.objects.get(pk=pk)
        for i in roles:
            employee.roles.add(Role.objects.get(pk=i))
    return redirect('employee_edit', pk=pk)


def delete_role_view(request, pk):
    if request.method == 'POST':
        role_id = request.POST['role']
        employee = Employee.objects.get(pk=pk)
        role = Role.objects.get(pk=role_id)
        employee.roles.remove(role)
    return redirect('employee_edit', pk=pk)

def employee_delete(request, pk):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=pk)
        employee.date_delete = datetime.now()
        employee.save()
    return redirect('employee_edit', pk=pk)

class AdminHalls(ListView):

    model = Service
    template_name = 'fitness/admin/halls.html'
    context_object_name = 'halls'
    queryset = Service.objects.filter(parent=None)
    paginate_by = 3


    def get(self, *args, **kwargs):
        resp = super().get(*args, **kwargs)
        return resp

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Залы'
        form = HallsForm(self.request.GET)
        context['form'] = form
        context['timetables'] = ServiceTimetable.objects.all()
        return context


class AdminHallSee(DetailView):
    model = Service
    template_name = 'fitness/admin/hall_see.html'
    context_object_name = 'hall'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Просмотр информации о зале'
        context['timetables'] = ServiceTimetable.objects.all()
        return context


class AdminHallUpdate(UpdateView):
    model = Service
    template_name = 'fitness/admin/hall_update.html'
    form_class = HallCreateForm
    context_object_name = 'hall'


    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['menu_admin'] = menu_admin
        context['title'] = 'Редактирование зала'
        context['timetables'] = ServiceTimetable.objects.all()

        return context

    def get_success_url(self):
        return reverse('hall_detail', kwargs={'pk': self.object.pk})


    def form_invalid(self, form):
        self.form_class = form
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return super().form_invalid(form)


def hall_delete(request, pk):
    if request.method == 'POST':
        hall = Service.objects.get(pk=pk)
        hall.date_delete = datetime.now()
        hall.save()
    return redirect('hall_edit', pk=pk)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")