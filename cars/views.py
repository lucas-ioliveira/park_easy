from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Car
from cars.service import CarService
from park_easy.repository import ParkEasyRepository

from ipdb import set_trace


class CarViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """

    def get(self, request):
        cars = CarService.service_get_all_or_one_cars(Car)
        return Response(cars.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CarService.service_post_or_update_car(request)
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
            car = CarService.service_get_all_or_one_cars(Car, pk)
        except Car.DoesNotExist:
            return Response(
                {"message": "Car not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(car.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            CarService.service_del_one_car(Car, pk)
        except Exception as e:
            return Response(
                {"message": "Car not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            car = ParkEasyRepository.repo_get_all_or_one_obj(Car, pk)

        except Car.DoesNotExist:
            return Response(
                {"message": "Car not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CarService.service_post_or_update_car(request, car)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
