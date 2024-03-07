from rest_framework import serializers
from .models import Vacancies

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'