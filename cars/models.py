from django.db import models

from clients_parking.models import Clients

from uuid import uuid4

class Car(models.Model):
    
    identifier = models.UUIDField(primary_key=True, default=uuid4, editable=False,
                              unique=True, verbose_name="Identifier")
    owner = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name="Owner")
    plate = models.CharField(max_length=255, verbose_name="Plate")
    color = models.CharField(max_length=255, verbose_name="Color")
    brand_car = models.CharField(max_length=255, verbose_name="Brand Car")
    model_car = models.CharField(max_length=255, verbose_name="Model Car")
    year_car = models.CharField(max_length=255, verbose_name="Year Car")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "car"
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.plate
