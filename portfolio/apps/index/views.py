# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(res):
    return render(res, "index/index.html")

def test(res):
    return render(res, "index/test.html")