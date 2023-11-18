from django.urls import path
from .views import EmployeeViewList, EmployeeViewDetail


urlpatterns = [
    path('', EmployeeViewList.as_view(), name='employee_list'),
    path('detail/<uuid:pk>/', EmployeeViewDetail.as_view(), name='employee_detail'),
]
