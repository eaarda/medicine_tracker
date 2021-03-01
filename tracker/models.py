from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=80)
    dosage = models.IntegerField()
    frequency = models.CharField(max_length=80)
