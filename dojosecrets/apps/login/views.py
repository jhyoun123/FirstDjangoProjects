# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Secret, Like
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    print User.objects.all()
    results = User.objects.register(request.POST)
    if results['valid']:
        request.session['name'] = User.objects.filter(email = request.POST['email'])[0].first
        request.session['id'] = User.objects.filter(email = request.POST['email'])[0].id
        request.session['type'] = "registered"
        return render(request, 'login/success.html')
    else:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')

def login(request):
    print User.objects.all()
    results = User.objects.login(request.POST)
    if results['valid']: 
        request.session['name'] = User.objects.filter(email = request.POST['login_email'])[0].first
        request.session['id'] = User.objects.filter(email = request.POST['login_email'])[0].id
        return redirect(reverse('secrets:secret_home'))
    else: 
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')