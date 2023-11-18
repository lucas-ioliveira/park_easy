from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
    job_title_name = serializers.SerializerMethodField()

    def get_job_title_name(self, obj):
        return obj.get_job_title_display()