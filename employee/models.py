from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    EMPLOYEE = 1
    MANAGER = 2

    JOB_TITLE_CHOICES = (
        
        (EMPLOYEE, 'Employee'),
        (MANAGER, 'Manager'),
    )

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, blank=True, null=True)
    job_title = models.SmallIntegerField(choices=JOB_TITLE_CHOICES, verbose_name="Job Title", blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name="Phone", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Address", blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name="City", blank=True, null=True)
    state = models.CharField(max_length=255, verbose_name="State", blank=True, null=True)
    country = models.CharField(max_length=255, verbose_name="Country", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "employee"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
    
    def __str__(self):
        return f'{self.user}'



