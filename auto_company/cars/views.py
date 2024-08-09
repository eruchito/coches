# cars/views.py

from django.shortcuts import render, get_object_or_404
from .models import Car, Buyer
from django.http import HttpResponseRedirect
from django.urls import reverse

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def buy_car(request, car_id):
    if request.method == 'POST':
        car = get_object_or_404(Car, pk=car_id)
        # Aquí podrías agregar la lógica para guardar la compra y el comprador
        return HttpResponseRedirect(reverse('car_list'))
