from django.urls import path
from reporting.views import ExportarRelatorioView

urlpatterns = [
    path('exportar/', ExportarRelatorioView.as_view(), name='exportar_relatorio'),
]