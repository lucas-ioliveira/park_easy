from django.db import models
from employee.models import Employee
from clients_parking.models import Clients
from cars.models import Car


class Parking(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Employee",
        related_name="parking_employee",
        blank=True,
        null=True,
    )
    client = models.ForeignKey(
        Clients,
        on_delete=models.CASCADE,
        verbose_name="Client",
        related_name="parking_client",
        blank=True,
        null=True,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name="Car",
        related_name="parking_car",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    entry = models.DateTimeField(
        verbose_name="Entry", auto_now_add=True, blank=True, null=True
    )
    output = models.DateTimeField(verbose_name="Output", null=True, blank=True)
    total_time = models.TimeField(verbose_name="Total Time", null=True, blank=True)
    amount_payable = models.CharField(
        verbose_name="Amount Payable", max_length=255, null=True, blank=True
    )

    db_table = "parking"
    verbose_name = "Parking"
    verbose_name_plural = "Parkings"

    def __str__(self):
        return f"{self.employee.user.first_name} - {self.client.first_name} - {self.car.plate}"
