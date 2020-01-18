'''
Urls.py file for Core module
'''
from django.urls import path
from .views import index
urlpatterns = [
    path(r'', index),
    path(r'index', index, name="index"),
]
