# cars/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
    path('', views.car_list, name='car_list'),
]
