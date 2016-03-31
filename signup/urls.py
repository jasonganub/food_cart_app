from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.create_seeker, name='create_seeker'),
]
