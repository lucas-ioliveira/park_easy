from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

class UserViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """
    def get(self, request):
        users = User.objects.filter(is_active=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewDetail(APIView):
    """
    Retrieves a single user and serializes it using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (uuid): The primary key of the user to retrieve.
    Returns:
        Response: The serialized data of the user.
    """
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
           
        
        
