from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Car
from .serializers import CarSerializer

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
        cars = Car.objects.filter(is_active=True)
        serializer = CarSerializer(cars, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CarSerializer(data=request.data)
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
            car = Car.objects.get(pk=pk)

        except Car.DoesNotExist:
            return Response({'message': 'Car not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({'message': 'Car not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)
        
        car.is_active = False
        car.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)

        except Car.DoesNotExist:
            return Response({'message': 'Car not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
           
        
        
