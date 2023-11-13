from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Not Use
    first_name = models.CharField(("first name"), max_length=150, blank=True, editable=False)
    last_name = models.CharField(("last name"), max_length=150, blank=True, editable=False)

    name = models.CharField(max_length=20)
