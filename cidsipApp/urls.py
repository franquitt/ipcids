from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('actualizar', views.actualizar, name = 'actualizar'),
]