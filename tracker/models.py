from django.db import models

# Create your models here.


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=80)
    dosage = models.IntegerField()
    frequency = models.CharField(max_length=80)
