from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.display_all_companies, name='browse'),
]
