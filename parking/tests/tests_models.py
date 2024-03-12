from django.test import TestCase
from django.contrib.auth.models import User
from employee.models import Employee
from cars.models import Car
from clients_parking.models import Clients
from parking.models import Parking
from django.utils import timezone


class ParkingTest(TestCase):

    def setUp(self):

        User.objects.create(
            id=1,
            username="Teste01",
            password="Teste01",
            email="Teste01@email.com",
            first_name="Teste01",
            last_name="Teste01",
            is_staff=True,
        )
        user_instancia = User.objects.first()
        Employee.objects.create(
            user=user_instancia,
            job_title=1,
            phone="11111111111",
            address="Rua teste",
            city="Cidade Teste",
            state="Estado teste",
            country="Pais teste",
            is_active=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

        Clients.objects.create(
            id=1,
            first_name="teste",
            last_name="teste",
            email="teste@email.com",
            phone="11111111111",
            address="rua teste",
            city="rua teste",
            state="rua teste",
            country="rua teste",
            is_active=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

        cliente_instancia = Clients.objects.first()
        Car.objects.create(
            owner=cliente_instancia,
            plate="abc1d12",
            color="branco",
            brand_car="volkswagen",
            model_car="Golf",
            year_car="2023",
            is_active=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

    def test_create_vacancies(self):
        employee_instancia = Employee.objects.first()
        car_instancia = Car.objects.first()
        cliente_instancia = Clients.objects.first()
        Parking.objects.create(
            employee=employee_instancia,
            client=cliente_instancia,
            car=car_instancia,
            is_active=True,
            created_at=timezone.now(),
            entry=timezone.now(),
            output=None,
            total_time=None,
            amount_payable=None,
        )
