# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print "*"
    return render(request, 'first_app/index.html')

def show(request):
    print "show"
    return render(request, 'first_app/show.html')