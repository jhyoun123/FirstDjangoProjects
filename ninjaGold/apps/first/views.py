# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def process_money(request):
    string = ""
    if 'gold' not in request.session: 
	    request.session['gold'] = 0
    if 'activities' not in request.session:
	    request.session['activities'] = []
    if request.POST['building'] == 'farm':
	    gold = random.randrange(10, 21)
    elif request.POST['building'] == 'cave':
	    gold = random.randrange(5, 11)
    elif request.POST['building'] == 'house':
	    gold = random.randrange(2, 6)
    elif request.POST['building'] == 'casino':
	    gold = random.randrange(-50, 51)

    if gold > 0:
	    string = 'Earned ' + str(gold) + ' golds from the ' + str(request.POST['building']) + '!'
    else:
	    string = 'Entered a casino and lost ' + str(gold) + ' golds... Ouch...'

    time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
    string += ' (' + str(time) + ')'
    request.session['gold'] += gold
    request.session['activities'].append(string)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
