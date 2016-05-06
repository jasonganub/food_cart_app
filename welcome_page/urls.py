from django.conf.urls import patterns, include, url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
	url(r'^', TemplateView.as_view(template_name='welcome.html'))
]