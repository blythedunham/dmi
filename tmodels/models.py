from django.db import models
from typedmodels.models import TypedModel

# Example from https://github.com/craigds/django-typed-models


class TypedAnimal(TypedModel):
    """
    Abstract model
    """
    name = models.CharField(max_length=255)

    def say_something(self):
        raise NotImplementedError

    def __repr__(self):
        return u'<%s: %s>' % (self.__class__.__name__, self.name)


class Canine(TypedAnimal):
    breed = models.CharField(
        max_length=200,
        null=True,
    )

    def say_something(self):
        return "woof"


class Feline(TypedAnimal):
    mice_eaten = models.IntegerField(
        default=0,
        null=True,
    )

    def say_something(self):
        return "meoww"
