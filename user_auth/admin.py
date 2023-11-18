from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    
    list_display = ('identifier', 'first_name', 'last_name', 'email', 'phone','job_title',
                     'is_active', 'is_admin', 'created_at', 'updated_at')
    list_filter = ('first_name','job_title', 'is_active', 'is_admin')
    search_fields = list_filter