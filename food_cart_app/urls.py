from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/', include('seeker.urls'), name='signup'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout',
                                {'next_page': '/'}, name='logout'),
    url(r'^browse/', include('query.urls'), name='browse'),
    url(r'^', TemplateView.as_view(template_name='landing_page.html')),
]
