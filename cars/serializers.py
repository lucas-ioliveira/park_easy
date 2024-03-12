from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    owner_first_name = serializers.SerializerMethodField()

    def get_owner_first_name(self, obj):
        return obj.owner.first_name
