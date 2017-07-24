from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='book_home'),
    url(r'^add_home$', views.add_home),
    url(r'^add$', views.add_review),
]