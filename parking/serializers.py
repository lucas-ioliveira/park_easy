from rest_framework import serializers
from .models import Vacancies, Parking
from cars.serializers import CarSerializer

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'


class ParkingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parking
        fields = '__all__'
    
        
    employee_name = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    car = CarSerializer()

    def get_employee_name(self, obj):
        return obj.employee.user.first_name
    
    def get_client_name(self, obj):
        return obj.client.first_name