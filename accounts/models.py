from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Subscriber(models.Model):
    user = models.OneToOneField(get_user_model(), unique=True, on_delete=models.CASCADE)
    interest = models.CharField(max_length=20, null=False)
