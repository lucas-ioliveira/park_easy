from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from park_easy.service import ParkEasyService
from park_easy.repository import ParkEasyRepository

from employee.models import Employee
from employee.serializers import EmployeeSerializer, UserSerializer


class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """

    def get(self, request):
        employees = ParkEasyService.service_get_all_or_one(model=Employee, app_serializer=EmployeeSerializer)
        return Response(employees.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ParkEasyService.service_post_or_update(request=request, app_serializer=EmployeeSerializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewDetail(APIView):
    """
    Retrieves a single user and serializes it using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (uuid): The primary key of the user to retrieve.
    Returns:
        Response: The serialized data of the user.
    """

    def get(self, request, pk):
        try:
            employee = ParkEasyService.service_get_all_or_one(model=Employee, app_serializer=EmployeeSerializer, pk=pk)
        except Employee.DoesNotExist:
            return Response(
                {"message": "Employee not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(employee.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            ParkEasyService.service_del_one(model=Employee, pk=pk)
        except Employee.DoesNotExist:
            return Response(
                {"message": "Employee not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            employee = ParkEasyRepository.repo_get_all_or_one_obj(model=Employee, pk=pk)
        except Employee.DoesNotExist:
            return Response(
                {"message": "Employee not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ParkEasyService.service_post_or_update(request=request, obj=employee, app_serializer=EmployeeSerializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
