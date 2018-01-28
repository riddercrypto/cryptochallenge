from django.db import models

# Create your models here.

# Model Knight
class Knight(models.Model):
    sir_name = models.CharField(max_length=100)
    public_api = models.CharField(max_length=50)
    secret_api = models.CharField(max_length=50)
