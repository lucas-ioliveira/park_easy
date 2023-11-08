from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'firt_name', 'last_name', 'email', 'job_title', 'is_admin', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_admin', 'is_active']
    search_fields = ['id_user', 'firt_name', 'last_name', 'email', 'job_title', 'is_admin', 'is_active', 'created_at', 'updated_at']