# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        if 'count' not in request.session:
            request.session['count'] = 1
        else: 
            request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/results')

    else:
        return redirect('/')

def results(request):
    return render(request, 'survey/results.html')