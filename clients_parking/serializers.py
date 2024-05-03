from rest_framework import serializers
from .models import Clients


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"
