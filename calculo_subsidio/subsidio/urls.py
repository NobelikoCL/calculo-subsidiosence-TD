# subsidio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_subsidio, name='calcular_subsidio'),
]
