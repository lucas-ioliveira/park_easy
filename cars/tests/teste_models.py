from django.test import TestCase
from cars.models import Car
from clients_parking.models import Clients
from django.utils import timezone


class CarTest(TestCase):

    data = {
        'owner_id': 1,
        'plate': 'abc1d23',
        'color': 'preto',
        'brand_car': 'nissan',
        'model_car': 'gtr r34',
        'year_car': '2019',  # Corrigido removendo o espaço extra
        'is_active': True,
        'created_at': timezone.now(),  # Utilize timezone.now() em vez de datetime.now()
        'updated_at': timezone.now(),  # Utilize timezone.now() em vez de datetime.now()
    }

    def test_create_car(self):
        Car.objects.create(
            owner_id=self.data['owner_id'],
            plate=self.data['plate'],
            color=self.data['color'],
            brand_car=self.data['brand_car'],
            model_car=self.data['model_car'],
            year_car=self.data['year_car'],
            is_active=self.data['is_active'],
            created_at=self.data['created_at'],
            updated_at=self.data['updated_at']
        )

        self.assertEqual(Car.objects.count(), 1)
