from django.db import models
from uuid import uuid4
import bcrypt


class Base(models.Model):

    identifier = models.UUIDField(primary_key=True, default=uuid4, editable=False,
                          unique=True, verbose_name="Identifier")
    first_name = models.CharField(max_length=255, verbose_name="First Name", blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name="Last Name", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", unique=True, blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name="Phone", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Address", blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name="City", blank=True, null=True)
    state = models.CharField(max_length=255, verbose_name="State", blank=True, null=True)
    country = models.CharField(max_length=255, verbose_name="Country", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True


class Employee(Base):

    EMPLOYEE = 1
    MANAGER = 2

    JOB_TITLE_CHOICES = (
        (EMPLOYEE, 'Employee'),
        (MANAGER, 'Manager'),
    )
    password = models.CharField(max_length=255, verbose_name="Password")
    job_title = models.SmallIntegerField(choices=JOB_TITLE_CHOICES,verbose_name="Job Title")
    is_admin = models.BooleanField(default=False, verbose_name="Is Admin")
    
    class Meta:
        db_table = "employee"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
    def set_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        hashed_password = self.password.encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        super(Employee, self).save(*args, **kwargs)