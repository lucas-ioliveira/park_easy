from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from park_easy.service import ParkEasyService
from park_easy.repository import ParkEasyRepository

from vacanciens.models import Vacancies
from vacanciens.serializers import VacanciesSerializer


class VacanciesViewList(APIView):
    """
    Retrieves all users and serializes them using the UserSerializer.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        Response: The serialized data of all users.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        vacancies = ParkEasyService.service_get_all_or_one(model=Vacancies, app_serializer=VacanciesSerializer)
        return Response(vacancies.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ParkEasyService.service_post_or_update(request=request, app_serializer=VacanciesSerializer)
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

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            vacancies = ParkEasyService.service_get_all_or_one(model=Vacancies,app_serializer=VacanciesSerializer, pk=pk)
        except Vacancies.DoesNotExist:
            return Response(
                {"message": "Vacancies not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(vacancies.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            ParkEasyService.service_del_one(model=Vacancies, pk=pk)
        except Vacancies.DoesNotExist:
            return Response(
                {"message": "Vacancies not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            vacancie = ParkEasyRepository.repo_get_all_or_one_obj(model=Vacancies, pk=pk)
        except Vacancies.DoesNotExist:
            return Response(
                {"message": "Vacancies not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = VacanciesSerializer(vacancie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
