from django.db import models
from uuid import uuid4
import bcrypt


class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False, 
                               unique=True, verbose_name="Id User")
    firt_name = models.CharField(max_length=255, verbose_name="First Name", blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name="Last Name", blank=True, null=True)
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=255, verbose_name="Password")
    job_title = models.CharField(max_length=255, verbose_name="Job Title")
    is_admin = models.BooleanField(default=False, verbose_name="Is Admin")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def set_password(self, raw_password):
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, raw_password):
        hashed_password = self.password.encode('utf-8')
        return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password)


