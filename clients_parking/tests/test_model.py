from django.test import TestCase
from clients_parking.models import Clients
from django.utils import timezone


class ClientTest(TestCase):

    def test_create_client(self):
        Clients.objects.create(
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
        self.assertEqual(Clients.objects.count(), 1)
