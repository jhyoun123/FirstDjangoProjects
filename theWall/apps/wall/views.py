# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User, Message, Comment
# Create your views here.

def index(request):
    return render(request, 'wall/index.html')

def register(request):
    if request.method == 'POST':
        User.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email = request.POST['email'], password = request.POST['pass'])
        users = User.objects.all()
        for user in users:
            print user.email, user.password
        return redirect('/')
    else:
        return redirect('/')
