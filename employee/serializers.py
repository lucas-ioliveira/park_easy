from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    user_first_name = serializers.SerializerMethodField()
    job_title_name = serializers.SerializerMethodField()

    def get_job_title_name(self, obj):
        return obj.get_job_title_display()

    def get_user_first_name(self, obj):
        return obj.user.first_name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_staff",
        )
        extra_kwargs = {"password": {"write_only": True}}
