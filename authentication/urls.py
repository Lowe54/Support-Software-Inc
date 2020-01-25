'''
URL File for Authentication module
'''
from django.urls import path
from .views import login, logout, profile_view
urlpatterns = [
    path(r'login', login, name="login"),
    path(r'logout', logout, name="logout"),
    path(r'profile', profile_view, name="profile")
]
