# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datatime

from django.shortcuts import render

# Create your views here.
def index(res):
    context = {
        "date": datetime.date.today(),
        "time": datetime.datetime.now().time()
    }
    return render(res, 'timedisplay/index.html', context)