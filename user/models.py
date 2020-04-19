from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Role:
    CUSTOMER_SERVICE = 'customer_service'
    PENJAHIT = 'penjahit'
    PEMOTONG = 'pemotong'
    ADMIN = 'admin'


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    role = CharField(blank=False, max_length=25, default=Role.ADMIN)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
