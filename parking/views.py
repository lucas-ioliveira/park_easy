from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Parking, Vacancies
from .serializers import ParkingSerializer, VacanciesSerializer
from park_easy.settings import MINUTES_PARKING_30, MINUTES_PARKING_60
from park_easy.settings import VALUE_PARKING_30, VALUE_PARKING_60, VALUE_PARKING_ADD_HOUR

from django.utils import timezone
from datetime import datetime

from datetime import timedelta

from ipdb import set_trace


class VacanciesViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """
    def get(self, request):
        vacancies = Vacancies.objects.filter(is_active=True)
        serializer = VacanciesSerializer(vacancies, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = VacanciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacanciesViewDetail(APIView):
    """
    Retrieves a single user and serializes it using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (uuid): The primary key of the user to retrieve.
    Returns:
        Response: The serialized data of the user.
    """
    def get(self, request, pk):
        vacancies = Vacancies.objects.get(pk=pk)
        serializer = VacanciesSerializer(vacancies)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        vacancie = Vacancies.objects.get(pk=pk)
        vacancie.is_active = False
        vacancie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        vacancie = Vacancies.objects.get(pk=pk)
        serializer = VacanciesSerializer(vacancie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParkingViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """
    def get(self, request):
        parking = Parking.objects.filter(is_active=True)
        serializer = ParkingSerializer(parking, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParkingViewDetail(APIView):
    """
    Retrieves a single user and serializes it using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (uuid): The primary key of the user to retrieve.
    Returns:
        Response: The serialized data of the user.
    """
    def get(self, request, pk):
        parking = Parking.objects.get(pk=pk)
        serializer = ParkingSerializer(parking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        parking = Parking.objects.get(pk=pk)
        parking.is_active = False
        parking.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        set_trace()
        try:
            parking = Parking.objects.get(pk=pk)
        except Parking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Parking not found")
        
        serializer = ParkingSerializer(parking, data=request.data, partial=True)

        if serializer.is_valid():
            entry = parking.entry
            output = timezone.now()

            total_time = entry - output 

            if total_time <= timedelta(minutes=MINUTES_PARKING_30):
                amount_payable = VALUE_PARKING_30
            elif total_time <= MINUTES_PARKING_60:
                amount_payable = VALUE_PARKING_60
            else:
                amount_payable = amount_payable + VALUE_PARKING_ADD_HOUR

            parking.total_time = total_time.timestrftime('%H:%M:%S')
            parking.amount_payable = str(amount_payable)
            parking.output = output
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
