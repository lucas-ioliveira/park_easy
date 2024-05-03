from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from parking.models import Parking
from parking.serializers import ParkingSerializer

from vacanciens.models import Vacancies

from park_easy.repository import ParkEasyRepository
from park_easy.service import ParkEasyService




class ParkingViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """

    def get(self, request):
        parking = ParkEasyService.service_get_all_or_one(model=Parking, app_serializer=ParkingSerializer)
        return Response(parking.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ParkEasyService.service_post_or_update(request=request, app_serializer=ParkingSerializer)
        if serializer.is_valid():
            ParkEasyRepository.repo_vacancie_occupied(model=Vacancies)
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
            parking = ParkEasyService.service_get_all_or_one(model=Parking, app_serializer=ParkingSerializer, pk=pk)
        except Parking.DoesNotExist:
            return Response(
                {"message": "Parking not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(parking.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            ParkEasyService.service_del_one(model=Parking, pk=pk)
        except Parking.DoesNotExist:
            return Response(
                {"message": "Parking not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            parking = ParkEasyRepository.repo_get_all_or_one_obj(model=Parking, pk=pk)
        except Parking.DoesNotExist:
            return Response(
                {"message": "Parking not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ParkEasyService.service_post_or_update(request=request, obj=parking, app_serializer=ParkingSerializer)

        if serializer.is_valid():

            ParkEasyRepository.repo_calculates_amount_payable(obj=parking)
            ParkEasyRepository.repo_vacancie_free(model=Vacancies)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
