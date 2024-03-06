from django.urls import path
from .views import EmployeeViewList, EmployeeViewDetail, UserCreateAPIView


urlpatterns = [
    path('', EmployeeViewList.as_view(), name='employee_list'),
    path('detail/<int:pk>/', EmployeeViewDetail.as_view(), name='employee_detail'),
    path('users/create/', UserCreateAPIView.as_view(), name='user_create'),
]
