from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Clients
from .serializers import EmployeeSerializer

class ClientViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """
    def get(self, request):
        clients = Clients.objects.filter(is_active=True)
        serializer = EmployeeSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientViewDetail(APIView):
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
            client = Clients.objects.get(pk=pk)
        except Clients.DoesNotExist:
            return Response({'message': 'Client not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            client = Clients.objects.get(pk=pk)
        except Clients.DoesNotExist:
            return Response({'message': 'Client not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)
        client.is_active = False
        client.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        try:
            client = Clients.objects.get(pk=pk)
        except Clients.DoesNotExist:
            return Response({'message': 'Client not found or non-existent'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
           
        
        
