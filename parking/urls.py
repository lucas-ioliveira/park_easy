from django.urls import path
from .views import ParkingViewList, ParkingViewDetail


urlpatterns = [
    path("", ParkingViewList.as_view(), name="parking_list"),
    path("detail/<int:pk>/", ParkingViewDetail.as_view(), name="parking_list_detail"),
]
