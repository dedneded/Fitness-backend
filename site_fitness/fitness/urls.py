from django.urls import path, re_path
from .views import *

urlpatterns = [

    path('', Home.as_view(), name='home'), #http://127.0.0.1:8000/
    path('halls/', Halls.as_view(), name='halls'),
    path('trainers/', Trainers.as_view(), name='trainers'),
    path('reviews/', reviews, name='reviews'),
    path('sales/', sales, name='sales'),
    path('subscriptions/', Subscriptions.as_view(), name='subscriptions'),
    path('login/', login, name='login'),

    path('categories/<slug:catid>/', categories), #http://127.0.0.1:8000/categories/1/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]