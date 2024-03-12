from django.db import models


class Base(models.Model):

    first_name = models.CharField(
        max_length=255, verbose_name="First Name", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255, verbose_name="Last Name", blank=True, null=True
    )
    email = models.EmailField(verbose_name="Email", unique=True, blank=True, null=True)
    phone = models.CharField(
        max_length=255, verbose_name="Phone", blank=True, null=True
    )
    address = models.CharField(
        max_length=255, verbose_name="Address", blank=True, null=True
    )
    city = models.CharField(max_length=255, verbose_name="City", blank=True, null=True)
    state = models.CharField(
        max_length=255, verbose_name="State", blank=True, null=True
    )
    country = models.CharField(
        max_length=255, verbose_name="Country", blank=True, null=True
    )
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True


class Clients(Base):

    class Meta:
        db_table = "client"
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self) -> str:
        return self.first_name
