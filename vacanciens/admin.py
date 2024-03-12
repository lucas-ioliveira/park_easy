from django.contrib import admin

from .models import Vacancies


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "total_number_vacancies",
        "vacancies_occupied",
        "vacancies_free",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = list_filter
