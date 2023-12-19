from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = ('identifier', 'plate', 'color', 'model_car', 'owner', 'is_active', 'created_at', 'updated_at')
    list_filter = ('plate', 'owner',)
    search_fields = list_filter
