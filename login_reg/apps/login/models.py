# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
# Create your models here.
class UserManager(models.Manager):
    def login(self, email, password, request):
        valid = True
        if len(User.objects.filter(email = email)) == 0:
            messages.error(request, "No email found")
            valid = False
        else: 
            if User.objects.filter(email = email)[0].password != password:
                messages.error(request, "Incorrect Password")
                valid = False
        return valid

    def register(self, first, last, email, password, confirm, request):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        valid = True
        if len(first) < 2 or not first.isalpha():
            messages.error(request, "First name is not valid")
            valid = False
        if len(last) < 2 or not last.isalpha():
            messages.error(request, "Last name is not valid")
            valid = False
        if not EMAIL_REGEX.match(email):
            messages.error(request, "Invalid Email Address!")
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters")
            valid = False
        if password != confirm:
            messages.error(request, "Passwords must match")
            valid = False  
        if valid:
            User.objects.create(first = first, last = last, email = email, password = password)
        return valid

class User(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __str__(self):
        return self.first + " " + self.last