from django.urls import path, include, re_path
from base import views
from .views import Show

urlpatterns = [
    path('', views.base, name = 'base' ), # Перый аргумент адрес, второй вьюха, третий - ...
    re_path('^(?P<pk>\d+)/$', Show.as_view(), name = 'Show' ), # метод as_view
]