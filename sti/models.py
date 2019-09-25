from django.db import models

# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=30)


class Boat(Vehicle):
    class Meta:
        proxy = True


class Car(Vehicle):
    class Meta:
        proxy = True
