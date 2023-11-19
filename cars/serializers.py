from rest_framework import serializers
from .models import Car
from clients_parking.models import Clients


class CarSerializer(serializers.Serializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=Clients.objects.all())

    class Meta:
        model = Car
        fields = '__all__'