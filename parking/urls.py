from django.urls import path
from .views import VacanciesViewList, VacanciesViewDetail


urlpatterns = [
    path('', VacanciesViewList.as_view(), name='vacancies_list'),
    path('detail/<uuid:pk>/', VacanciesViewDetail.as_view(), name='vacancies_detail'),
]
