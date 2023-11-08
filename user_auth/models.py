from django.db import models
from uuid import uuid4
import bcrypt


class User(models.Model):
    EMPLOYEE = 1
    MANAGER = 2

    JOB_TITLE_CHOICES = (
        (EMPLOYEE, 'Employee'),
        (MANAGER, 'Manager'),
    )

    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False, 
                               unique=True, verbose_name="Id User")
    firt_name = models.CharField(max_length=255, verbose_name="First Name", blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name="Last Name", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", unique=True)
    password = models.CharField(max_length=255, verbose_name="Password")
    job_title = models.SmallIntegerField(choices=JOB_TITLE_CHOICES,verbose_name="Job Title")
    is_admin = models.BooleanField(default=False, verbose_name="Is Admin")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
    def set_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        hashed_password = self.password.encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


