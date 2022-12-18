from .models import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Залы", 'url_name': 'halls'},
        {'title': "Тренеры", 'url_name': 'trainers'},
        {'title': "Отзывы", 'url_name': 'reviews'},
        {'title': "Акции", 'url_name': 'sales'},
        {'title': "Абонементы", 'url_name': 'subscriptions'},
        {'title': "Личный кабинет", 'url_name': 'login'}
]


class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                services = Service.objects.all()
                context['services'] = services
                context['menu'] = menu
                return context