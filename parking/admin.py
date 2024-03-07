from django.contrib import admin
from .models import Parking


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'employee', 'client', 'car', 'is_active', 'created_at', 'entry', 
                    'output', 'total_time', 'amount_payable')
    list_filter = ('employee', 'client', 'car', 'is_active')
    search_fields = list_filter
