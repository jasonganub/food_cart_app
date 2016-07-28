from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from login import views
from django.views.generic import TemplateView



urlpatterns = [
    # Examples:
    # url(r'^$', 'food_cart_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'login/', 'django.contrib.auth.views.login'),
    url(r'logout/', 'django.contrib.auth.views.logout'),
    url(r'^signup/', include('signup.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^welcome/', include('welcome_page.urls')),
    url(r'^', TemplateView.as_view(template_name='landing_page.html')),
]
