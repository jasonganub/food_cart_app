from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^$', include(router.urls)),
]
