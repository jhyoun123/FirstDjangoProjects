# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class ReviewManager(models.Manager):
    def addReview(self, postData, request):
        results = {"valid": True, "errors": []}
        if not postData['title']:
            results['valid'] = False
            results['errors'].append("You must give the title of a book")
        if not postData['review']:
            results['valid'] = False
            results['errors'].append("Please give a short review of the book")
        if results['valid']:
            if not postData['new_author']:
                author = postData['author_list']
            else:
                author = postData['new_author']
            if len(Book.objects.filter(title = postData['title'])) == 0:
                Book.objects.create(title = postData['title'], author = author)

            Review.objects.create(book = Book.objects.get(title = postData['title']), user = User.objects.get(id = request.session['id']), content = postData['review'], rating = int(postData['rating']))
        return results

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    content = models.TextField(max_length=1000)
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    objects = ReviewManager()
    def __str__(self):
        return self.book.title + " " + self.user.first