from django.db import models

from uuid import uuid4

from user_auth.models import Employee
from clients_parking.models import Clients
from cars.models import Car


class Vacancies(models.Model):

    identifier = models.UUIDField(primary_key=True, default=uuid4, editable=False,
                                  unique=True, verbose_name="Identifier")
    number_vacancies = models.IntegerField(verbose_name="Number Vacancies")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    db_table = "vacancies"
    verbose_name = "Vacancies"
    verbose_name_plural = "Vacancies"

    def __str__(self):
        return str(self.identifier)


class Parking(models.Model):

    '''
        Valores do estacionamento:
        30 min - R$8,00
        60 min - R$15,00
        a cada hora após 60 min - R$3,00
        24 horas - R$30,00
        
    '''

    identifier = models.UUIDField(primary_key=True, default=uuid4, editable=False,
                                  unique=True, verbose_name="Identifier")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Employee")
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name="Client")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Car")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    entry = models.DateTimeField(verbose_name="Entry", auto_now_add=True)
    output = models.DateTimeField(verbose_name="Output", null=True, blank=True)
    total_time = models.DateTimeField(verbose_name="Total Time", null=True, blank=True)
    amount_payable = models.FloatField(verbose_name="Amount Payable", null=True, blank=True)

    db_table = "parking"
    verbose_name = "Parking"
    verbose_name_plural = "Parkings"

    def __str__(self):
        return str(self.identifier)
