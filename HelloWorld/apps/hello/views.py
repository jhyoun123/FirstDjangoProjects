# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(res):
    print "hello world"
    return render(res, "hello/index.html")
