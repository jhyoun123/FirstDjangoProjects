# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Review
# Create your views here.
def index(request):
    if (request.session['status']):
        context = {
            "reviews": Review.objects.all(),
        }
        return render(request, 'books/index.html', context)
    else: 
        messages.error(request, "Please log in first")
        return redirect('/')

def add_home(request): 
    if (request.session['status']):
        return render(request, 'books/add_home.html')
    else: 
        messages.error(request, "Please log in first")
        return redirect('/')

def add_review(request):
    results = Review.objects.addReview(request.POST, request)
    print Review.objects.all()

    if results['valid']:
        return render(request, 'books/books.html')
    else:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/books/add_home')