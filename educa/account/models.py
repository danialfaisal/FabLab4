from django.db import models
from django.conf import settings
from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.utils import timezone


class User(AbstractUser):
    def is_instructor(self):
        if hasattr(self, 'instructor'):
            return True
        return False


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
