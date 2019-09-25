from django.db import models


class Animal(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=255)

    def speak(self):
        "##?!"


class Giraffe(Animal):
    spots = models.IntegerField()

    def speak(self):
        return "Hum"  # infrasonic communication


class Zebra(Animal):
    stripes = models.IntegerField()

    def speak(self):
        return "Whinny"
