from rest_framework import serializers
from .models import Parking


class ParkingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parking
        fields = '__all__'
    
        
    employee_name = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    infos = serializers.SerializerMethodField()

    def get_employee_name(self, obj):
        return obj.employee.user.first_name
    
    def get_client_name(self, obj):
        return obj.client.first_name
    
    def get_infos(self, obj):
        infos = {
            "car": {
                "plate": obj.car.plate,
                "color": obj.car.color,
                "brand_car": obj.car.brand_car,
                "model_car": obj.car.model_car,
                "year_car": obj.car.year_car,
            }
        }
        return infos