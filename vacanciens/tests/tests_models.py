from django.test import TestCase
from vacanciens.models import Vacancies
from django.utils import timezone

class TestVacancies(TestCase):


    def test_create_vacancies(self):
        Vacancies.objects.create(
            total_number_vacancies = 10,
            vacancies_occupied = 0,
            vacancies_free  = 0,
            is_active = True,
            created_at = timezone.now(),
            updated_at = timezone.now(),
        )

        self.assertEquals(Vacancies.objects.count(), 1)

