from django.urls import path
from .views import CarViewList, CarViewDetail


urlpatterns = [
    path("", CarViewList.as_view(), name="car_list"),
    path("detail/<int:pk>/", CarViewDetail.as_view(), name="car_detail"),
]
