from django.contrib import admin
from employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "job_title",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "id",
        "user",
        "job_title",
        "is_active",
    )
    search_fields = list_filter
