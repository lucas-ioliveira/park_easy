from django.urls import path
from .views import VacanciesViewList, VacanciesViewDetail, ParkingViewList, ParkingViewDetail


urlpatterns = [
    path('list/', VacanciesViewList.as_view(), name='vacancies_list'),
    path('list/detail/<int:pk>/', VacanciesViewDetail.as_view(), name='vacancies_detail'),
    path('', ParkingViewList.as_view(), name='parking_list'),
    path('detail/<int:pk>/', ParkingViewDetail.as_view(), name='parking_list_detail'),

]
