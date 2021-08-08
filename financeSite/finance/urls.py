from django.urls import path
from . import views
# app urls.py
urlpatterns = [
    path('', views.index, name='index')
]