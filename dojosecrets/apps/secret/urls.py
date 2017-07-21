from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='secret_home'),
    url(r'^post$', views.post),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^like/(?P<id>\d+)$', views.like),
]