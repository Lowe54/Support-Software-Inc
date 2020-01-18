'''
URL File for Authentication module
'''
from django.urls import path
from .views import login, logout
urlpatterns = [
    path(r'login', login, name="login"),
    path(r'logout', logout, name="logout")
]
