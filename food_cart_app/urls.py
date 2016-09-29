from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'food_cart_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/register/', include('seeker.urls'), name='signup'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login',
                                {'next_page': '/'}, name='login'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout',
                                {'next_page': '/'}, name='logout'),
    url(r'^', TemplateView.as_view(template_name='landing_page.html')),
    url(r'^admin/', include(admin.site.urls)),
]
