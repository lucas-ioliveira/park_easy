from django.urls import path
from .views import UserViewList, UserViewDetail


urlpatterns = [
    path('', UserViewList.as_view(), name='user_list'),
    path('detail/<uuid:pk>/', UserViewDetail.as_view(), name='user_detail'),
]
