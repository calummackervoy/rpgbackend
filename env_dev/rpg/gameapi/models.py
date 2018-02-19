from __future__ import unicode_literals

from django.db import models

# Create your models here

class ImageContent(models.Model):
    # below: models.URLField()?
    src = models.CharField(max_length=100, null=True)
    priority = models.PositiveSmallIntegerField(default=0)

class TextContent(models.Model):
    text = models.CharField(max_length=255)
    priority = models.PositiveSmallIntegerField(default=0)

class Option(models.Model):
    text = models.CharField(max_length=255)
    # TODO: some way of linking this option to an action/function

class Page(models.Model):
    title = models.CharField(max_length=100, null=True)
    # should below be many-to-one? then duplicate images/text that are reused,
    # with new priorities
    content = models.ManyToManyField(TextContent)
    images = models.ManyToManyField(ImageContent)
    options = models.ManyToManyField(Option)
