# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

import random

# Create your views here.
def index(res):
    return render(res, "randomGenerator/index.html")

def create(res):
    res.session['string'] = ''.join(random.choice('0123456789ABCDEF') for i in range(14))
    if 'count' not in res.session:
        res.session['count'] = 0
    else: 
        res.session['count'] += 1  
    return redirect('/')