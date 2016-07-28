from django.conf.urls import patterns, include, url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
	url(r'^', views.verify_authentication, name='verify_authentication')
]