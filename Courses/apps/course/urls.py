from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^course/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^remove/(?P<id>\d+)$', views.remove),
]