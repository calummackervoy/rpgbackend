from __future__ import unicode_literals

from django.db import models

# Create your models here

class ImageContent(models.Model):
    # below: models.URLField()?
    src = models.CharField(max_length=100, null=True)
    priority = models.PositiveSmallIntegerField(default=0)
    #tells Python how to display a human-readable representation of an object
    def __str__(self):
        return self.src

    class Meta:
        ordering = ['priority']

class TextContent(models.Model):
    text = models.CharField(max_length=255)
    priority = models.PositiveSmallIntegerField(default=0)
    #tells Python how to display a human-readable representation of an object
    def __str__(self):
        return self.text

    class Meta:
        ordering = ['priority']

class Option(models.Model):
    text = models.CharField(max_length=255)
    # TODO: some way of linking this option to an action/function
    #tells Python how to display a human-readable representation of an object
    def __str__(self):
        return self.text

class Page(models.Model):
    title = models.CharField(max_length=100, null=True)
    # should below be many-to-one? then duplicate images/text that are reused,
    # with new priorities
    content = models.ManyToManyField(TextContent)
    images = models.ManyToManyField(ImageContent)
    options = models.ManyToManyField(Option)
    #tells Python how to display a human-readable representation of an object
    def __str__(self):
        return self.title
