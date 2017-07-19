# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def add(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
        "info": Course.objects.get(id=id)
    }
    return render(request, 'course/remove.html', context)

def remove(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')