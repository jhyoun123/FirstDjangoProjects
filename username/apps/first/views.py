# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def add(request):
    valid = User.objects.register(request.POST['username'])
    if valid:
        return redirect('/success')
    else:
        messages.error(request, "Username is not valid")
        return redirect('/')

def success(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'first/success.html', context)