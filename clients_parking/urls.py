from django.urls import path
from .views import ClientViewList, ClientViewDetail


urlpatterns = [
    path("", ClientViewList.as_view(), name="client_list"),
    path("detail/<int:pk>/", ClientViewDetail.as_view(), name="client_detail"),
]
