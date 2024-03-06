from django.contrib import admin
from .models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country',
                     'is_active','created_at', 'updated_at')
    list_filter = ('first_name', 'email', 'phone')
    search_fields = list_filter




