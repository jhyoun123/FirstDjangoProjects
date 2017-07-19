# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    valid = User.objects.register(request.POST['first'], request.POST['last'], request.POST['email'], request.POST['pass'], request.POST['confirm'], request)

    if valid:
        request.session['name'] = User.objects.filter(email = request.POST['email'])[0].first
        request.session['type'] = "registered"
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
    print User.objects.all()
    context = {
        "users" : User.objects.all()
    }
    return render(request, 'login/success.html', context)

def login(request):
    valid = User.objects.login(request.POST['login_email'], request.POST['login_pass'], request)
    
    if valid: 
        request.session['name'] = User.objects.filter(email = request.POST['login_email'])[0].first
        request.session['type'] = "logged in"
        return redirect('/success')
    else: 
        return redirect('/')