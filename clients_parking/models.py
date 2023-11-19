from django.db import models
from user_auth.models import Base


class Clients(Base):

    class Meta:
        db_table = "client"
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
    def __str__(self) -> str:
        return self.first_name
