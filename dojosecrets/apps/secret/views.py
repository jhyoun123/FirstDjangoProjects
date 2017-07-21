# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..login.models import User, Secret, Like

# Create your views here.
def index(request):
    context = {
        'secrets': Secret.objects.all().order_by('-date_added'),
    }
    if (request.session['status']):
        return render(request, 'secret/index.html', context)
    else:
        messages.error(request, "Please log in first.")
        return redirect('/')

def post(request): 
    Secret.objects.create(content = request.POST['secret_content'], user = User.objects.get(id = request.session['id']))
    print Secret.objects.all()
    return redirect('/secrets')

def delete(request, id): 
    Secret.objects.get(id = id).delete()
    print Secret.objects.all()
    return redirect('/secrets')

def like(request, id): 
    Like.objects.create(user = User.objects.get(id = request.session['id']), secret = Secret.objects.get(id = id))
    return redirect('/secrets')