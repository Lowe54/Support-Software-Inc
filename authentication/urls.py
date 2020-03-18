'''
URL File for Authentication module
'''
from django.urls import path

from .views import (get_profile_edit_form, import_user_data, login, logout,
                    profile_view, register, save_profile)

urlpatterns = [
    path(r'login', login, name="login"),
    path(r'logout', logout, name="logout"),
    path(r'profile', profile_view, name="profile"),
    path(r'register', register, name="register"),
    path(r'profile/edit/', get_profile_edit_form),
    path(r'profile/save/', save_profile),
    
    path(r'importuser', import_user_data)
]
