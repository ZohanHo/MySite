from django.urls import path, include
from base import views

urlpatterns = [
    path('', views.base, name = 'base' ), # Перый аргумент адрес, второй вьюха, третий - ...
]