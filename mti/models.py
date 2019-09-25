from django.db import models


class BigCat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self} ({self.id})>"

    def speak(self):
        return "meow"


class Lion(BigCat):
    giraffes_hunted = models.IntegerField()

    def speak(self):
        return "roar"


class Cheetah(BigCat):
    pass
