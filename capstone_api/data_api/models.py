from django.db import models

# Create your models here.
class VacationEvent(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    notes = models.TextField(blank=True)

