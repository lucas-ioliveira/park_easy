from django.test import TestCase
from employee.models import Employee
from django.contrib.auth.models import User
from django.utils import timezone


class EmployeeTest(TestCase):

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

    def test_create_employee(self):
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

        self.assertEqual(Employee.objects.count(), 1)
