from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Vacancies
from .serializers import VacanciesSerializer


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
        try:
            vacancies = Vacancies.objects.get(pk=pk)
        except Vacancies.DoesNotExist:
            return Response(
                {"message": "Vacancies not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = VacanciesSerializer(vacancies)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            vacancie = Vacancies.objects.get(pk=pk)
        except Vacancies.DoesNotExist:
            return Response(
                {"message": "Vacancies not found or non-existent"},
                status=status.HTTP_404_NOT_FOUND,
            )
        vacancie.is_active = False
        vacancie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            vacancie = Vacancies.objects.get(pk=pk)
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
