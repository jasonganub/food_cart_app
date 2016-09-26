from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'food_cart_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^welcome/', include('welcome_page.urls')),
    url(r'^', TemplateView.as_view(template_name='landing_page.html')),
    url(r'^admin/', include(admin.site.urls)),
]
