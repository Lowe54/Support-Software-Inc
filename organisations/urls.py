'''
Url's.py file for Organisation App
'''
from django.urls import path

from .views import (add_or_edit_organisation, associate_users,
                    get_unassociated_users, get_user_list, save_organisation,
                    show_organisation_list, unassocate_user)

urlpatterns = [
    path(r'list', show_organisation_list, name="show_organisation_list"),
    path(r'add/', add_or_edit_organisation, name="add_organisation"),
    path(r'edit/', add_or_edit_organisation, name="edit_organisation"),
    path(r'userlist/', get_user_list, name="get_organisation_users"),
    path(r'save/', save_organisation, name="save_organisation"),
    path(r'getunassociated/', get_unassociated_users),
    path(r'associate/', associate_users),
    path(r'unassociate/', unassocate_user)
]
