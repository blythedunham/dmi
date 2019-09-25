
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    title = models.CharField(max_length=255)
    body = models.TextField(null=True)


class Blog(models.Model):
    name = models.CharField(max_length=255)
    comments = GenericRelation(Comment)
