from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Car
from cars.serializers import CarSerializer
from park_easy.repository import ParkEasyRepository
from park_easy.service import ParkEasyService


class CarViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """

    def get(self, request):
        cars = ParkEasyService.service_get_all_or_one(model=Car, app_serializer=CarSerializer)
        return Response(cars.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ParkEasyService.service_post_or_update(request, app_serializer=CarSerializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarViewDetail(APIView):
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
            car = ParkEasyService.service_get_all_or_one(model=Car, pk=pk, app_serializer=CarSerializer)
        except Car.DoesNotExist:
            return Response(
                {"message": "Car not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(car.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            ParkEasyService.service_del_one(model=Car, pk=pk)
        except Exception as e:
            return Response(
                {"message": "Car not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            car = ParkEasyRepository.repo_get_all_or_one_obj(model=Car, pk=pk)

        except Car.DoesNotExist:
            return Response(
                {"message": "Car not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ParkEasyService.service_post_or_update(request, car=car, app_serializer=CarSerializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
