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
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():

    #         try:
    #             job_title_request = request.data.get('job_title')
    #             if job_title_request:
    #                 if type(job_title_request) != int:
    #                     return Response({'error': 'Job title must be an integer'}).status_code(status.HTTP_400_BAD_REQUEST)
    #                 else:
    #                     job_title = User.objects.filter(job_title=job_title_request)
    #         except:
    #             return Response({'error': 'Job title must be an integer'}).status_code(status.HTTP_404_NOT_FOUND)
            
        
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        
        
           
        
        
