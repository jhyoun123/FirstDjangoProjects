# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def login(self, postData):
        results = {"valid": True, "errors": []}
        if len(User.objects.filter(email = postData['login_email'])) == 0:
            results['errors'].append("No email found")
            results['valid'] = False
        else: 
            if User.objects.filter(email = postData['login_email'])[0].password != postData['login_pass']:
                results['errors'].append("Incorrect Password")
                results['valid'] = False
        return results

    def register(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        results = {"valid": True, "errors": []}
        # for user in User.objects.all():
        #     user.delete()
        if not postData['first'] or len(postData['first']) < 2 or not postData['first'].isalpha():
            results['errors'].append("First name is not valid")
            results['valid'] = False
        if not postData['last'] or len(postData['last']) < 2 or not postData['last'].isalpha():
            results['errors'].append("Last name is not valid")
            results['valid'] = False
        if not postData['email'] or not EMAIL_REGEX.match(postData['email']):
            results['errors'].append("Invalid Email Address!")
            results['valid'] = False
        if not postData['pass'] or len(postData['pass']) < 8:
            results['errors'].append("Password must be at least 8 characters")
            results['valid'] = False
        if postData['pass'] != postData['confirm']:
            results['errors'].append("Passwords must match")
            results['valid'] = False
        if results['valid']:
            if len(User.objects.filter(email = postData['email'])) != 0:
                results['errors'].append("Please try another email")
                results['valid'] = False
            else: 
                User.objects.create(first = postData['first'], last = postData['last'], email = postData['email'], password = postData['pass'])
        return results

class User(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __str__(self):
        return self.first + " " + self.last + " " + self.password

class Secret(models.Model):
    content = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.content + " " + self.user.first

class Like(models.Model):
    user = models.ForeignKey(User)
    secret = models.ForeignKey(Secret, related_name="likes")
    date_added = models.DateTimeField(auto_now_add=True)