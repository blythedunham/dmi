from django.db import models


class ElfManager(models.Manager):

    def get_queryset(self):
        return super(ElfManager, self).get_queryset(
        ).filter(person_type='e')

    def create(self, **kwargs):
        kwargs.update({'person_type': 'e'})
        return super(ElfManager, self).create(**kwargs)


class Person(models.Model):
    name = models.CharField(max_length=255)
    person_type = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self} ({self.id})>"

    def characteristic(self):
        return "Middle Earth dweller"


class Hobbit(Person):

    class Meta:
        proxy = True

    def characteristic(self):
        return "hairy feet"


class Elf(Person):

    objects = ElfManager()

    class Meta:
        proxy = True

    def characteristic(self):
        return "immortal"
