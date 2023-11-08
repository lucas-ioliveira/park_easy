from django.urls import path
from .views import UserViewList


urlpatterns = [
    path('', UserViewList.as_view(), name='user_list'),
    # path('detail/<int:pk>/', SolicitacaoViewDetail.as_view(), name='solicitacao_detail'),
]
