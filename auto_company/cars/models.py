# cars/models.py

from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)  # Marca del coche
    model = models.CharField(max_length=100)  # Modelo del coche
    year = models.IntegerField()  # Año de fabricación
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    description = models.TextField()  # Descripción del coche
    image = models.ImageField(upload_to='car_images/')  # Imagen del coche

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Nombre del comprador
    email = models.EmailField()  # Correo electrónico
    phone = models.CharField(max_length=15)  # Teléfono

    def __str__(self):
        return self.name
