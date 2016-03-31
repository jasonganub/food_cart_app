from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from signup import urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'food_cart_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^login/', include('login.urls')),
    url(r'^signup/', include('signup.urls'))
]
