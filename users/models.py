from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    email = models.EmailField(_('Adresse mail'), unique=True)
    phone_number = models.CharField(max_length=13)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone_number']