from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from park_easy.repository import ParkEasyRepository
from park_easy.service import ParkEasyService

from clients_parking.models import Clients
from clients_parking.serializers import ClientsSerializer


class ClientViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """

    def get(self, request):
        clients = ParkEasyService.service_get_all_or_one(model=Clients, app_serializer=ClientsSerializer)
        return Response(clients.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ParkEasyService.service_post_or_update(request=request, app_serializer=ClientsSerializer)
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
            client = ParkEasyService.service_get_all_or_one(model=Clients, pk=pk, app_serializer=ClientsSerializer)
        except Clients.DoesNotExist:
            return Response(
                {"message": "Client not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(client.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            ParkEasyService.service_del_one(model=Clients, pk=pk)
        except Exception as e:
            return Response(
                {"message": "Client not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            client = ParkEasyRepository.repo_get_all_or_one_obj(model=Clients,pk=pk)
        except Clients.DoesNotExist:
            return Response(
                {"message": "Client not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ParkEasyService.service_post_or_update(request=request, obj=client, app_serializer=ClientsSerializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
