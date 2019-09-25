from django.db import models


class SnowGiraffe(models.Model):
    name = models.CharField(max_length=255)


class Tongue(models.Model):
    color = models.CharField(max_length=255)
    giraffe = models.OneToOneField(
        SnowGiraffe,
        on_delete=models.CASCADE,
        auto_created=True,
        default=None,
    )


class Leg(models.Model):
    toe_count = models.IntegerField()
    giraffe = models.ForeignKey(
        SnowGiraffe,
        on_delete=models.CASCADE
    )
