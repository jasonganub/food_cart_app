from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.register_user, name='register'),
]
