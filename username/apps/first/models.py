# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register(self, data):
        if len(data) > 8 and len(data) < 26:
            User.objects.create(username = data)
            return True
        else: 
            return False

class User(models.Model):
    username = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __str__(self):
        return self.username