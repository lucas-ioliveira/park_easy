from django.db import models

class Vacancies(models.Model):

    total_number_vacancies = models.IntegerField(verbose_name="Total Number Vacancies", blank=True, null=True)
    vacancies_occupied = models.IntegerField(verbose_name="Total Number Vacancies occupied", blank=True, null=True)
    vacancies_free  = models.IntegerField(verbose_name="Total Number Free Vacancies", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    db_table = "vacancies"
    verbose_name = "Vacancies"
    verbose_name_plural = "Vacancies"

    def __str__(self):
        return f'{self.total_number_vacancies}'