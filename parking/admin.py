from django.contrib import admin

from .models import Parking, Vacancies


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):

    list_display = ('identifier', 'number_vacancies', 'is_active', 'created_at', 'updated_at')
    list_filter = ('number_vacancies', 'is_active')
    search_fields = list_filter


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    
    list_display = ('identifier', 'employee', 'client', 'car', 'is_active', 'created_at', 'entry', 
                    'output', 'total_time', 'amount_payable')
    list_filter = ('employee', 'client', 'car', 'is_active')
    search_fields = list_filter
