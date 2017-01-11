from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.display_all_companies, name='browse'),
    url(r'^(?P<id>[0-9]+)/$', views.display_company_by_id, name='browse_by_id'),
]
