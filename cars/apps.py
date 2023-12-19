from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
    verbose_name = 'Car'
    verbose_name_plural = 'Cars'
