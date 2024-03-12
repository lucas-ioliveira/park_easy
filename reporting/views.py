from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime, timedelta
from parking.models import Parking


class ExportarRelatorioView(APIView):
    def get(self, request, *args, **kwargs):
        # http://127.0.0.1:8000/api/v1/reporting/exportar/?data=2024-03-06 00:00:00&employee=1&cliente=1
        data = request.query_params.get("data")
        employee = request.query_params.get("employee")
        client = request.query_params.get("cliente")

        if not any([data, employee, client]):
            return Response(
                {"message": "Nenhum parâmetro fornecido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        parking = Parking.objects.all()

        if data:
            data_format = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
            parking = parking.filter(
                created_at__gte=data_format,
                created_at__lte=data_format + timedelta(days=1),
            )
            pdf_filename = f"relatorio_vendas_data_{data}.pdf"
            self.exportar_para_pdf(parking, pdf_filename)

        if employee:
            parking = parking.filter(employee=employee)
            pdf_filename = f"relatorio_vendas_employee_{employee}.pdf"
            self.exportar_para_pdf(parking, pdf_filename)

        if client:
            parking = parking.filter(client=client)
            pdf_filename = f"relatorio_vendas_client_{client}.pdf"
            self.exportar_para_pdf(parking, pdf_filename)

        # Construir a resposta PDF
        response = FileResponse(
            open(pdf_filename, "rb"), content_type="application/pdf"
        )
        response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'

        if pdf_filename:
            os.remove(pdf_filename)

        return response

    def exportar_para_pdf(self, queryset, filename):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        header_style = styles["Heading1"]
        conteudo = [Paragraph("Relatório de Vendas", header_style)]
        table_data = [["data", "employee", "client"]]

        for item in queryset:
            table_data.append([item.created_at, item.employee, item.client])

        table = Table(table_data)
        doc.build(conteudo + [table])
