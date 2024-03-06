from django.db import models
from clients_parking.models import Clients


class Car(models.Model):
    
    owner = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name="Owner", blank=True, null=True)
    plate = models.CharField(max_length=255, verbose_name="Plate", unique=True, blank=True, null=True)
    color = models.CharField(max_length=255, verbose_name="Color", blank=True, null=True)
    brand_car = models.CharField(max_length=255, verbose_name="Brand Car", blank=True, null=True)
    model_car = models.CharField(max_length=255, verbose_name="Model Car", blank=True, null=True)
    year_car = models.CharField(max_length=255, verbose_name="Year Car", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "car"
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.plate
