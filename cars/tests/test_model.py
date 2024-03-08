from django.test import TestCase
from cars.models import Car
from clients_parking.models import Clients
from django.utils import timezone

class CarTest(TestCase):

    def setUp(self):
        Clients.objects.create(
            id=1, 
            first_name = 'teste',
            last_name = 'teste',
            email = 'teste@email.com',
            phone = '11111111111',
            address = 'rua teste',
            city = 'rua teste',
            state = 'rua teste',
            country = 'rua teste',
            is_active = True,
            created_at = timezone.now(),
            updated_at = timezone.now(),
        )

    def test_create_car(self):
        cliente_instancia = Clients.objects.first()  
        Car.objects.create(
            owner=cliente_instancia,
            plate='abc1d12',
            color='branco',
            brand_car='volkswagen',
            model_car='Golf',
            year_car='2023',
            is_active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        self.assertEqual(Car.objects.count(), 1)
