from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Parking
from .serializers import ParkingSerializer
from vacanciens.models import Vacancies
from park_easy.settings import MINUTES_PARKING_30, MINUTES_PARKING_60
from park_easy.settings import VALUE_PARKING_30, VALUE_PARKING_60, VALUE_PARKING_ADD_HOUR

from datetime import timedelta


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

            vacancies_id = 2
            vacancies = Vacancies.objects.filter(id=vacancies_id).first()
            total_vacancies = vacancies.total_number_vacancies
            vacancies.vacancies_occupied = int(vacancies.vacancies_occupied + 1)
            vacancies.vacancies_free = int(total_vacancies - 1)
            vacancies.save()
            
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
        try:
            parking = Parking.objects.get(pk=pk)
        except Parking.DoesNotExist:
            return Response({'message': 'Parking not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ParkingSerializer(parking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            parking = Parking.objects.get(pk=pk)
        except Parking.DoesNotExist:
            return Response({'message': 'Parking not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)
        
        parking.is_active = False
        parking.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        try:
            parking = Parking.objects.get(pk=pk)
        except Parking.DoesNotExist:
            return Response({'message': 'Parking not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ParkingSerializer(parking, data=request.data, partial=True)

        if serializer.is_valid():
            entry = parking.entry
            output = timezone.now()

            total_time = output - entry

            if total_time <= timedelta(minutes=MINUTES_PARKING_30):
                amount_payable = VALUE_PARKING_30
            elif total_time <= timedelta(minutes=MINUTES_PARKING_60):
                amount_payable = VALUE_PARKING_60
            else:
                amount_payable = amount_payable + VALUE_PARKING_ADD_HOUR

            parking.total_time = str(total_time)
            parking.amount_payable = str(amount_payable)
            parking.output = output

            vacancies_id = 2
            vacancies = Vacancies.objects.filter(id=vacancies_id).first()
            vacancies.vacancies_occupied = int(vacancies.vacancies_occupied - 1)
            vacancies.vacancies_free = int(vacancies.vacancies_free + 1)
            vacancies.save()

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
