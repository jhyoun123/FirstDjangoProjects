# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.title + " " + self.author