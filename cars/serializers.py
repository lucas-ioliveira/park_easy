from rest_framework import serializers
from .models import Car
from clients_parking.models import Clients


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'